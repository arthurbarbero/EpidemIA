class preliminary_diagnosis():    
    def __init__(self, b=0.3, k=1, symptoms = pd.DataFrame(), diseases = pd.DataFrame()):
        self.b = b
        self.k = k
        self.all_symptoms = symptoms
        self.all_diseases = diseases
        
        
    def bm25_weight(data, K1=1, B=0.3):
        """ Weighs each row of the matrix data by BM25 weighting """
        # calculate idf per term (symptom)
        N = float(data.shape[0])
        idf = np.log(N / (1 + np.bincount(data.col)))

        # calculate length_norm per document (disease)
        row_sums = np.squeeze(np.asarray(data.sum(1)))
        average_length = row_sums.sum() / N
        length_norm = (1.0 - B) + B * row_sums / average_length

        # weight matrix rows by bm25
        ret = coo_matrix(data)
        ret.data = ret.data * (K1 + 1.0) / (K1 * length_norm[ret.row] + ret.data) * idf[ret.col]
        return ret
    
    
    def fit(self, filename, separator):
        """ Reads in the dataset, and returns a tuple of a pandas dataframe and a sparse matrix of symptom/disease/severity """
        data = pd.read_csv(filename, 
                           separator, 
                           usecols=[0,1,2], 
                           names=['symptom', 'disease','severities'], 
                           skiprows=1)

        data=data.dropna()

        # map each disease and symptom to a unique numeric value
        data['symptom'] = data['symptom'].astype("category")
        data['disease'] = data['disease'].astype("category")

        # create a sparse matrix of all the symptoms/severities
        sev = coo_matrix((data['severities'].astype(float),
                           (data['disease'].cat.codes.copy(),
                            data['symptom'].cat.codes.copy())))

        self.data = data
        self.matrix = sev
        self.sum_disease = data.groupby(['disease']).severities.sum()
        self.symptom = data['symptom'].cat.codes.copy()
        
        self.symptom_count = data.groupby('symptom').size()
        
        Ur, Si, VTr = svds(bm25_weight(self.matrix), k=100)
        VTr = pd.DataFrame(VTr)
        
        self.dataset_result = pd.DataFrame(cosine_similarity(Ur,VTr.T), columns=self.symptom_count.index, index=list(self.sum_disease.index)) 

    def get_diseases_by_symptoms(self, symptom_id):
        print("Sintoma ", (self.all_symptoms[self.all_symptoms['Symptom_id'] == symptom_id])['Symptom_desc'].values[0])
        print("Top 10 prováveis doênças relacionadas")
        print("--------------------------------------")
        listProb = self.dataset_result[symptom_id].sort_values(ascending=False).index
        for x in listProb[:10]:
            print(x, self.all_diseases[self.all_diseases['Disease_id'] == x].Disease_desc.values)
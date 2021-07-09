# EpidemIA
Python + Jupyter Notebook

## Integrantes :bust_in_silhouette:

- Arthur Barbero [LinkedIn](https://www.linkedin.com/in/arthur-barbero/) / [Github](https://github.com/arthurbarbero);
- Felippe Alves [LinkedIn](https://www.linkedin.com/in/felippe-alves-de-paula/) / [Github](https://github.com/FelippeAlves);
- Gabriel Landim [LinkeIn](https://www.linkedin.com/in/gabriel-landim-2b5bb8181/) / [Github](https://github.com/Glandim);
- José Vinícius [LinkedIn](https://www.linkedin.com/in/jose-vinicius-ferreira-santana-903239181/) / [Github](https://github.com/JViniciusF).
- Thyago Odorico [LinkeIn](https://www.linkedin.com/in/thyago-odorico-10ab8a11a/) / [Github](https://github.com/togarci).


## Objetivos :dart:

Este projeto tem como objetivo apresentar os conhecimentos adquiridos e a criação de uma IA baseada nas ferramentas acima para a avaliação da matéria de Intenligência Artificial da FATEC SJC (Faculdade de Tecnologia de São José dos Campos)

## Introdução :pencil:


2019 foi um ano que irá ficar nos arautos da história, principalmente pela grande pandemia de uma nova doença com origem nos países asiáticos, uma evolução da SARS, denominada COVID-19.

A ideia de passar novamente por uma epidemia assusta qualquer pessoa nos dias atuais, e olhando as ações que foram tomadas, a única forma de minimizar os problemas e causas é a rápida identificação e comunicação, ou seja, informação. 

Considerada como o novo petróleo, a informação é tida como o grande recurso dos dias atuais, e não são poucos os tipos de softwares que tentam acessar e coletar nossos dados dia após dia na esperança de vincular nossos dados ao consumo ou estilo de vida, para que as empresas possam oferecer seus serviços ou despontar à frente de seus concorrentes. 

Com essa visão, a informação também pode ser usada para o bem das sociedades, basta que consigamos reter informações dos usuários de forma inteligente, concisa e transparente.

Desta maneira, utilizaremos formas de capturar informações, retê-las e utilizá-las de forma a identificar novas doenças, padrões de relacionamento entre doenças-pacientes e doenças-sintomas, padrões de localidade e gerar insights de possíveis novas epidemias.

A Inteligência Artificial entra neste cenário auxiliando o projeto como um todo e se beneficiando de seus dados que serão coletados ao longo de seu uso visando a implementação de modelos treinados à uma aplicação WEB.

## Tecnologias utilizadas :computer:

- [Python 3.6](https://www.python.org/)
  - [Jupyter-notebook](https://jupyter.org/)
  - [Numpy](https://numpy.org/)
  - [Pandas](https://pandas.pydata.org/)
  - [Scikit-learn](https://scikit-learn.org/stable/)
  - [Scipy](https://www.scipy.org/)
  - [xgboost](https://xgboost.readthedocs.io/en/latest/)
  - [Scikitplot](https://scikit-plot.readthedocs.io/en/stable/Quickstart.html)

[Anaconda](https://www.anaconda.com/) for environment.
## Resultados encontrados 

Com os dados que possuimos e com todas nossas limitações, podemos perceber que nas avaliações realizadas, temos uma acurácia de cerca de 50% dos ranqueamentos e similaridades ocorridos em cima dos nossos dados de sintomas e doenças. 
Porém, identificamos que para aprendizados não-supervisionados, na maioria dos casos estudados, após a utilização dos algoritmos de ranqueamento e similaridade, o resultado encontrado pode ou não apresentar resultados favoráveis para seu objetivo, simplesmente por se tratar de  aprendizagem não supervisionada.

[*Mais detalhes*](https://github.com/arthurbarbero/EpidemIA/blob/main/EpidemiWeb.pdf)

## Requerimentos do projeto

Os resultados do projeto e seus códigos podem ser vistos no próprio Github, [clicando aqui](https://github.com/arthurbarbero/EpidemIA/blob/main/Exemplo.ipynb), porém, caso deseje rodar o projeto localmente, segue os requisitos:

- Python 3.6;
  - Bibliotecas podem ser encontradas [aqui](https://github.com/arthurbarbero/EpidemIA/blob/main/requirements.txt);
- Qualquer IDE;
- Jupyter Notebook.

## Como iniciar o projeto localmente

- **Clone o projeto:**
    ```python
        git clone https://github.com/arthurbarbero/EpidemIA.git
    ```

- **Crie um ambiente separado do seu python global e acesse:**
    
    ```python
        conda create --name epidemiia python=3.6
        conda activate epidemiia
    ```

    Para mais informações sobre criação de ambientes com Anaconda, [acesse aqui](https://docs.anaconda.com/anaconda/user-guide/getting-started/).


- **Instale as dependencias rapidamente pelo arquivo `requirements.txt`:**
    ``` python
        pip install -r requirements.txt
    ```

- **Inicie o jupyter notebook na raiz da pasta do seu repositório clonado:**
    ``` python
        jupyter notebook
    ```

    Este comando em seu terminal irá iniciar um servidor local iniciando também uma página do Chrome.
    A partir desta pagina acesse o arquivo Exemplo.ipynb e siga os passos do exemplo.
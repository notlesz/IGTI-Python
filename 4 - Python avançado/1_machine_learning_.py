# -*- coding: utf-8 -*-
"""1-  Machine Learning .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GBq8YRJlyt4Ph6Z2odT21ZO2aJvSOPq3

**KMEANS**
"""

from pandas import DataFrame
import matplotlib.pyplot as plt

#Criar dados aleatorios
dados = {'x':[12,10,21,45,78,96,45,11,4,7,9,44,22,78,43,7,15],
         'y':[99,72,23,35,45,41,42,11,7,8,9,6,44,21,36,31,30]}

# Criar o dataframe
df = DataFrame(dados,columns=('x','y'))
df.head()

#Adicionar a bliblioteca para construir o ambiente
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=2) #Cria o objeto de para o algoritmo k-means para encontrar 2 clusters
kmeans.fit(df) # Aplica o algoritmo
centroides = kmeans.cluster_centers_ #Encontra as coordenadas dos centroids
print(centroides)

# Realiza o plot do grafico de saida
plt.scatter(df['x'],df['y'], c=kmeans.labels_.astype(float), s = 50, alpha=0.5)
plt.scatter(centroides[:,0], centroides[:,1], c = 'red', s = 50)
plt.xlabel('x')
plt.ylabel('y')

"""**KNN**"""

#Importando bibliotecas
from sklearn import neighbors, datasets
import pandas as pd
import numpy as np

# Cria rotina para atualizar o dataset Iris
iris = datasets.load_iris()

# Convertendo o banco de dados IRIS para o dataframe
df_iris = pd.DataFrame(data = np.c_[iris['data'], iris['target']], 
                       columns = iris['feature_names']+['target'])

print(df_iris.head())

# Transformar dados em arrays
x = df_iris.iloc[:, :-1].values # Dados de entrada
y = df_iris.iloc[:, 4].values # Saidas ou target

# Realiza a divisão dos dados entre treinamento e teste
from sklearn.model_selection import train_test_split # Função que realiza a divisao do dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20) #divide 20% do teste

# Realiza o processo de normalização dos dados
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler() #Objeto que normaliza os dados
scaler.fit(x_train)

x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# Treinar o modelo
from sklearn.neighbors import KNeighborsClassifier
classifer = KNeighborsClassifier(n_neighbors = 5) # Ultiliza a construção por meio de 5 vizinhos
classifer.fit(x_train,y_train) # Aplica a classificação

# Realiza a previsão
y_pred = classifer.predict(x_test)

# Constroi a matriz de confusão para comprar o modelo criado
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Realiza o plot da matriz de confusão
matriz_confusao = confusion_matrix(y_test, y_pred)
from mlxtend.plotting import plot_confusion_matrix

fig, ax = plot_confusion_matrix(conf_mat=matriz_confusao)
plt.show()

"""**Arvore de decisção e SVM**"""

from sklearn.tree import DecisionTreeClassifier # Importa o classificador da arvore de decisao
from sklearn import metrics #Importa as métricas para avaliação

# Cria o objeto de classificação através do 
clf = DecisionTreeClassifier() 

# Realiza o treinamento do classificador
clf = clf.fit(x_train,y_train)

# Realiza a previsão de classificação
y_pred = clf.predict(x_test)

# Avaliando modelo

#Reealiza plot de matrix de confusão
matriz_confusao = confusion_matrix(y_test,y_pred)
from mlxtend.plotting import plot_confusion_matrix

fig, ax = plot_confusion_matrix(conf_mat=matriz_confusao)
plt.show()

# Visualização da árvore de decisão
# Impor das bibliotecas necessárias para realizar a visualização da árvore de decisão
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus

# Constroi a arvore de decisao para o DB Iris
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names = iris.feature_names,class_names=['0','1','2'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('iris.png')
Image(graph.create_png())

"""**Suppor Vector Machine(SVM)**"""

#Biblioteca necessáriia para a construção do SVM
from sklearn.svm import SVC # -> Classificador

# Cria objeto SVM
clf = SVC()

# Realiza a classificação via SVM
clf.fit(x_train,y_train)

# Realiza a previsão de classificação 
y_pred = clf.predict(x_test)

# Avaliando o modelo

# Realiza o plot de matrix  de confusão 
matriz_confusao = confusion_matrix(y_test, y_pred)
from mlxtend.plotting  import plot_confusion_matrix

fig, ax = plot_confusion_matrix(conf_mat=matriz_confusao)
plt.show()

"""**Exemplos de Redes Neurais**"""

# Definição da biblioteca
from sklearn.neural_network import MLPClassifier

# Define a configuração da rede
clf = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(5,5), random_state=1) #Rede com camadas escondidas até 5 neuronios cada

# Realiza o fit do modelo
clf.fit(x_train,y_train)

# Realiza a previsão
y_pred = clf.predict(x_test)

# Avaliando o modelo

# Realiza o plot da matriz de modelo
matriz_confusao = confusion_matrix(y_test,y_pred)
from mlxtend.plotting import plot_confusion_matrix

fig,ax = plot_confusion_matrix(conf_mat=matriz_confusao)
plt.show()

"""**Rede neural em DEEP LEARNING com TensorFLow**"""

from tensorflow.keras.layers import Input, Dense, Dropout, Activation
from tensorflow.keras.models import Model #Importando o modelo a ser empregado
import seaborn as sns #plotar o grafico

dataset = sns.load_dataset('iris')
dataset.head()

# Adivinhando entre entrada em saida]
x = dataset.drop(['species'],axis=1)
y = pd.get_dummies(dataset.species, prefix='output') #Transforma cada uma das classes em vetores

x.head() #Entradas

y.head() # Saidas

#Divide os dados entre treinamento e teste 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.20, random_state = 39)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(y_test)

entrada = input(shape=(x_train.shape[1],))
camada_1 = Dense(100, activation='relu')(entrada) 
camada_2 = Dense(50, activation='relu')(camada_1)
camada_3 = Dense(25, activation='relu')(camada_2)
saida = Dense(y_train.shape[1], activation='softmax')(camada_3)

model = Model(inputs = entrada, outputs = saida) #Define o modelo

model.summary()

model.compile(loss='categorical_crossentropy', optmizer = 'adam', metrics=['acc'])

# Realizando o treinamento da nossa rede
history = model.fit(x_train, y_train, batch_size=4, epochs = 20, verbose = 1, validation_split=0.20)

acuracia=model.evaluate(x_test,y_test,verbose=1) #Acuracia do modelo
print('Acuracia do modelo: ',acuracia[1])
#Cristian Ernesto Valle Flores - SMSS068623
#Diego Samuel Reyes Moreno - SMSS057423 
#importamos las librerias 
import pandas as pd
import matplotlib.pyplot as plt

#cargamos el dataset
df1 = pd.read_csv('crime_rankings_2020.csv')

#verificamos los tipos de datos
print(df1.dtypes)
#imprimira en pantalla los tipos de datos de cada columna del CSV

#seleccionamos las columnas y nos aseguramos que sean datos numericos
df1 = df1[['rank','safety_index']]
df1['safety_index'] = pd.to_numeric(df1['safety_index'], errors='coerce')#vericficara que sean datos
#de tipo numericos 

#creamos el grafico de lineas
df1.plot(kind='line', x='rank', y='safety_index', title='rangos de indices de seguridad')
#definimos los ejes X Y de la grafica
#title sera el titulo que aparecera en nuestra grafica 
plt.show()
#es una funcion, la cual mostrara nuestro grafico en pantalla

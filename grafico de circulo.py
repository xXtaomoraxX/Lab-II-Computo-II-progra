#Cristian Ernesto Valle Flores - SMSS068623
#Diego Samuel Reyes Moreno - SMSS057423 
#importtamos las librerias 
import pandas as pd
import matplotlib.pyplot as plt

#cargamos nuestro dataset
df1 = pd.read_csv('laptop_prices.csv')

#verificamos los tipos de datos
print(df1.dtypes)
#imprimira en pantalla los tipos de datos de cada columna del CSV

#seleccionamos las columnas y nos aseguramos que sean datos numericos
df1 = df1.head(20)[['Ram','Weight']]#volvemos a usar head por que la cantidad de datos del csv es muy grande
df1['Weight'] = pd.to_numeric(df1['Weight'], errors='coerce')##vericficara que sean datos
#de tipo numericos 

#creamos el grafico circular
df1.set_index('Ram').plot(kind='pie', y='Weight', title='distribucion de peso segun la ram', 
autopct='%1.1f%%')
#title sera el titulo que aparecera en nuestra grafica 
plt.ylabel('')
plt.show()
#es una funcion, la cual mostrara nuestro grafico en pantalla


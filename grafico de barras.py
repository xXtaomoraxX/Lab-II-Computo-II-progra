#Cristian Ernesto Valle Flores - SMSS068623
#Diego Samuel Reyes Moreno - SMSS057423 
#importamos las librerias 
import pandas as pd
import matplotlib.pyplot as plt

#cargamos el dataset
df1 = pd.read_csv('gym_members_exercise_tracking.csv')

#verificamos los tipos de datos
print(df1.dtypes)
#imprimira en pantalla los tipos de datos de cada columna del CSV

#seleccionamos las columnas y nos aseguramos que sean numericos
df1 = df1.head(20)[['Resting_BPM','Weight (kg)']]#usamos head para definir el rango de datos, por que el csv
#contiene muchos datos y se satura el grafico 
df1['Weight (kg)'] = pd.to_numeric(df1['Weight (kg)'], errors='coerce')#vericficara que sean datos
#de tipo numericos 


#creamos el grafico de barras
df1.plot(kind='bar', x='Weight (kg)', y='Resting_BPM', title='weight vs resting')
#definimos los ejes X Y de la grafica
#title sera el titulo que aparecera en nuestra grafica 
plt.show()
#es una funcion, la cual mostrara nuestro grafico en pantalla
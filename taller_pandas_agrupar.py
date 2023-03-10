# -*- coding: utf-8 -*-
"""Taller - Pandas: agrupar.ipynb
#prueba
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EAKvTP9YqnkRTLmKOIjE9PrE1UxhfnB-

#Taller Group by, count, value_counts

1. Cargar el CSV phone_data y convertir la columna date de string a tiempo
"""

import pandas as pd
import dateutil
 
data = pd.read_csv('phone_data.csv', index_col='index')
data
data['date'] = data['date'].apply(dateutil.parser.parse)
data

"""2. ¿Cuál fue el ítem (llamada/datos) de mayor duración? """

data['duration'].max()

data[data['duration']==data['duration'].max()]

data.loc[800:,['duration']].plot(kind='bar')

"""*   ¿Cuál fue la llamada de mayor duración?
*   ¿Cuál fue el evento de datos de mayor duración?
"""

print(data[(data['duration']==data['duration'].max()) & (data['item']=='call')])

print(data[data['duration']==data['duration'][data['item']=='data'].max()])

"""3. ¿Cuánto fue el total de segundos de todas las llamadas?"""

data['duration'][data['item'] == 'call'].sum()

"""

*   ¿Cuánto fue el total de segundos entre sms y eventos de datos?


"""

data['duration'][(data['item'] == 'sms') | (data['item'] == 'data')].sum()

"""4. ¿Cuantas entradas hay por cada uno de los meses"""

data['month']
data['month'].value_counts()

"""*   ¿Cuantas entradas de datos hay por cada uno de las redes?
*   ¿Cuantas entradas de llamada hay por cada una de las redes?


"""

data['month'][data['item'] == 'call'].value_counts()

data['network'][data['item'] == 'call'].value_counts()

"""5. Obtener la suma de la duración por mes"""

data['duration'].sum()
data.groupby('month')['duration'].sum()

"""* Obtener el promedio de duración de llamadas por cada una de las redes
* Obtener el promedio de duración de eventos de datos por cada una de las redes

"""

data[data['item']=='call'].groupby('network')['duration'].mean()

data[data['item']=='data'].groupby('network')['duration'].mean()

"""6. Obtener el número de entradas por mes"""

data.groupby('month').count()

data.groupby('month')['date'].count()
data['month'].value_counts()

"""* Obtener el número de entradas tipo llamada por cada una de las redes
* Obtener el número de entradas tipo sms por cada una de las redes

"""

data[data['item']=='call'].groupby('month').count()

data[data['item']=='call'].groupby('month')['month'].count()

data[data['item']=='sms']['network'].value_counts()

data[data['item']=='sms'].groupby('network')['network'].count()

"""7. Cuántos eventos de llamada, datos y sms hubo por mes"""

data.groupby(['month', 'item'])['date'].count()

"""* Por cada uno de los meses, ¿cuántas veces se usaron cada una de las redes (para cualquier evento)?
* Por cada uno de los meses, ¿cuántas veces se usaron cada una de las redes discriminando el tipo de evento?

"""

data.groupby(['month', 'network','item'])['date'].count()

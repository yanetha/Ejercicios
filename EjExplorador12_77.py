# -*- coding: utf-8 -*-
"""EjExplorador12_77.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s_00SeD56siHJ8OPmVLs2vNxt4jeHcS0
"""

#Manipulacion basica con pandas


import pandas as pd

# Paso 1
datos = pd.DataFrame({
    'Nombre': ['Ana', 'Juan', 'María', 'Carlos'],
    'Edad': [22, 30, 25, 28],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
})

# Paso 2
print("Información del DataFrame:")
print(datos)

# Paso 3
datos_filtrados = datos[datos['Edad'] > 25]
print("\nPersonas con edad mayor que 25:")
print(datos_filtrados)

# Paso 4
datos['Categoria'] = pd.cut(datos['Edad'], bins=[0, 25, float('inf')], labels=['Joven', 'Adulto'])

# Paso 5
print("\nDataFrame Actualizado:")
print(datos)
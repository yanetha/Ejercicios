# -*- coding: utf-8 -*-
"""EjExplorador8_51.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LrYTXKTr9fVgxURsUeOt_kMnE993lMF3
"""

#Contraseña

contrasena_correcta = "Ilovepython123"

while True:
    contrasena_ingresada = input("Ingrese la contraseña: ")
    if contrasena_ingresada == contrasena_correcta:
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        print("Contraseña incorrecta. Inténtelo nuevamente.")
# -*- coding: utf-8 -*-
"""EjExplorador8_50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yHMM0XGhXSGXqyz5DutNGU1V94Iz-Tt1
"""

#Ventas

ventas = [float(input(f"Ingrese las ventas del producto {i + 1}: ")) for i in range(3)]

producto_mas_costoso = max(ventas)
producto_mas_economico = min(ventas)
media_ventas = sum(ventas) / len(ventas)

print(f"Producto más costoso: {producto_mas_costoso}")
print(f"Producto más económico: {producto_mas_economico}")
print(f"Media de las ventas: {media_ventas}")
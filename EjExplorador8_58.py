# -*- coding: utf-8 -*-
"""EjExplorador8_58.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KY0KiuckvMchcbrOeXfaOzx_2_cCjZXD
"""

#Compras

total_compras = 0

while True:
    monto = float(input("Ingrese el monto de la compra (0 para finalizar): "))
    if monto == 0:
        break
    elif monto < 0:
        print("Monto inválido. Ingrese un valor positivo.")
    else:
        total_compras += monto

print(f"El total de las compras realizadas es: {total_compras}")
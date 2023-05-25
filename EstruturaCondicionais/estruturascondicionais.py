# -*- coding: utf-8 -*-
"""EstruturasCondicionais

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19GU3ekHgZ-cAKgYn5T3s3okNm9yDP9eN
"""

# Código para estruturas condicionais em Python

def Estruturas_condicionais():

  idade = 18

  # Estrutura if()

  if idade >= 18:
      print("Você é maior de idade.")

  # Estrutura if-else()

  if idade >= 18:
      print("Você é maior de idade.")
  else:
      print("Você é menor de idade.")

  # Estrutura if-elif-else()

  if idade < 18:
      print("Você é menor de idade.")
  elif idade >= 18 and idade < 65:
      print("Você é adulto.")
  else:
      print("Você é idoso.")
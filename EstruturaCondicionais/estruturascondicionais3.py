# -*- coding: utf-8 -*-
"""EstruturasCondicionais3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/105hKiQv5L0jSGBdB6snOYpNqw7mp4_WB
"""

# Estruturas condicionais 3

def Estruturas_Condicionais3():

# Estrutura while - Executa repetidamente um bloco de código enquanto uma condição específica for verdadeira
  contador = 0

  while contador < 5:
      print(contador)
      contador += 1


# Estrutura for - Itera sobre uma sequência (como uma lista, uma string, etc.) e executa um bloco de código para cada elemento da sequência

  numeros = ["um,", "dois", "tres"]

  for numero in numeros:
      print(numeros)


# Estrutura break - Encerra imediatamente o loop mais próximo em que está sendo executado

  numeros = [1, 2, 3, 4, 5]

  for numero in numeros:
      if numero == 3:
          break
      print(numero)


# Estrutura continue - Pula para a próxima iteração do loop mais próximo em que está sendo executado
  numeros = [1, 2, 3, 4, 5]

  for numero in numeros:
      if numero == 3:
          continue
      print(numero)

# Estrutura pass - É usado como um espaço reservado para um bloco de código vazio
  numero = 10

  if numero > 5:
      pass
  else:
      print("O número é menor ou igual a 5.")
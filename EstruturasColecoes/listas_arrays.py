# -*- coding: utf-8 -*-
"""Listas/arrays

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rUhhsbJyNSba_LvQazQu3JMuN_m_J9DN
"""

# Estrutura com coleções/conjutos/listas em Python.

# Funções para listas
# len(lista): Retorna o tamanho da lista, ou seja, o número de elementos.
# min(lista): Retorna o menor valor da lista (quando os elementos são comparáveis).
# max(lista): Retorna o maior valor da lista (quando os elementos são comparáveis).
# sum(lista): Retorna a soma de todos os elementos da lista (quando aplicável).
# index(): Retorna o índice da primeira ocorrência de um elemento na lista.
# pop(): Remove e retorna o elemento em uma posição específica da lista.

def Estrturas_colecoes():

  # Criação de diferentes tipos de listas
  lista_vazia = []
  numeros = [1, 2, 3, 4, 5]
  numeros = ["um", "dois", "tres"]
  lista_mista = [1, "dois", True, 3.14]

  # Acessando elementos de uma lista
  numeros = [1, 2, 3, 4, 5]
  print(numeros[0])  # Saída: 1
  print(numeros[2])  # Saída: 3
  print(numeros[-1])  # Saída: 5

  # Operações com listas
  numeros = ["um", "dois", "tres"]

  numeros.append("quatro")  # Adiciona um elemento ao final da lista
  numeros.remove("um")  # Remove um elemento específico da lista
  print(len(numeros))  # Obtém o tamanho da lista
  print("um" in numeros)  # Verifica se um elemento está presente na lista

  mais_numeros = ["cinco", "seis"]
  numeros.extend(numeros)  # Concatena duas listas

  print(numeros)  

  # Iteração em uma lista  
  for numero in numeros:
      print(numero)

  # Indexação e fatiamento
  numeros = [1, 2, 3, 4, 5]

  print(numeros[1])  # Saída: 2 (acessando o segundo elemento)
  print(numeros[2:4])  # Saída: [3, 4] (fatiando a lista a partir do terceiro até o quarto elemento)
  print(numeros[:3])  # Saída: [1, 2, 3] (fatiando a lista até o terceiro elemento)
  print(numeros[3:])  # Saída: [4, 5] (fatiando a lista a partir do quarto elemento até o final)
  print(numeros[::-1])  # Saída: [5, 4, 3, 2, 1] (revertendo a ordem da lista)

  # Cópia de listas: Ao atribuir uma lista a uma nova variável, você está criando uma nova referência para a mesma lista
  numeros = [1, 2, 3]
  copia = numeros.copy()  # Cria uma cópia independente da lista
  outra_copia = list(numeros)  # Outra forma de criar uma cópia independente

  numeros.append(4)

  print(copia)  # Saída: [1, 2, 3]
  print(outra_copia)  # Saída: [1, 2, 3]

  # Compreensão de listas: A compreensão de listas é uma forma concisa de criar listas com base em outra lista ou iterável, aplicando uma expressão ou uma lógica condicional.
  numeros = [1, 2, 3, 4, 5]

  dobro = [2 * num for num in numeros]
  print(dobro)  # Saída: [2, 4, 6, 8, 10]

  pares = [num for num in numeros if num % 2 == 0]
  print(pares)  # Saída: [2, 4]

  # Métodos de listas: As listas possuem vários métodos embutidos que permitem realizar diferentes operações, como ordenação, contagem de elementos, reversão e muito mais.

  numeros = [3, 1, 4, 2, 5]

  numeros.sort()  # Ordena a lista em ordem crescente
  print(numeros)  # Saída: [1, 2, 3, 4, 5]

  print(numeros.count(2))  # Saída: 1 (conta o número de ocorrências do elemento 2)

  numeros.reverse()  # Inverte a ordem da lista
  print(numeros)  # Saída: [5, 4, 3, 2, 1]
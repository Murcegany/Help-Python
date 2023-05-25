# -*- coding: utf-8 -*-
"""FuncoesMatematicas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfRKxLvHNn1yGafr-scctmxQNoL22YMK
"""

# Código para funções matemáticas em Python
import math

def matemáticas():

  x = 16

  print(math.sqrt(x))  # Retorna a raiz quadrada de um número -> sqrt()
    # Saída: 4.0

  print(math.pow(2, 3))  # Retorna o resultado da potência de um número pelo outro -> pow()
    # Saída:8.0

#######################################################################################################

  y = 3.7

  print(math.ceil(y))  # Retorna o menor número inteiro maior ou igual a um dado número -> ceil()
    # Saída: 4

  print(math.floor(y))  # Retorna o maior número inteiro menor ou igual a um dado número -> floor()
    # Saída: 3

  print(round(y)) # Retorna o numéro arrendodado para o valor mais próximo -> round()
    # Saída: 4

#######################################################################################################

  z = -10

  print(math.abs(z)) # Retorna o valor absoluto de um número -> abs()
    # Saída: 10

#######################################################################################################

  # Funções trigonométricas que retornam o seno, cosseno e tangente de um ângulo em radianos 
  angulo = math.pi/4

  print(math.sin(angulo)) # -> sin()
    # Saída: 0.7071067811865476

  print(math.cos(angulo)) # -> cos()
    # Saída: 0.7071067811865476

  print(math.tan(angulo)) # -> tan()
   # Saída: 0.9999999999999999

#######################################################################################################

# Retorna o logaritmo na base de um número -> log()

  a = 10

  print(math.log(a)) # Retorna o logaritmo natural (base e) de um número ou o logaritmo na base especificada -> log()
    # Saída: 2.302585092994046

#######################################################################################################

# Retorna o logaritmo na base 10 de um número -> log10()

  b = 100

  print(math.log10(b)) # Retorna o logaritmo na base 10 de um número -> log10()
    # Saída: 2.0

#######################################################################################################

# Retorna o valor exponencial (e elevado à potência x) -> exp()

  c = 2

  print(math.exp(c))  
    # Saída: 7.3890560989306495

#######################################################################################################

# Funções hiperbólicas que retornam o seno hiperbólico, cosseno hiperbólico e tangente hiperbólica de um número

  d = 1

  print(math.sinh(x))  
    # Saída: 1.1752011936438014 
  print(math.cosh(x))  
    # Saída: 1.5430806348152437
  print(math.tanh(x))  
    # Saída: 0.7615941559557649

#######################################################################################################

# Converte um ângulo de radianos para graus -> degrees()

  angulo_radianos = math.pi/4
  angulo_graus = math.degrees(angulo_radianos)

  print(angulo_graus)  
    # Saída: 45.0

#######################################################################################################

# Converte um ângulo de graus para radianos -> radians()

  angulo_graus = 180
  angulo_radianos = math.radians(angulo_graus)
  print(angulo_radianos)  
    # Saída: 3.141592653589793

#######################################################################################################

# Retorna o fatorial de um número -> factorial()

  e = 5
  print(math.factorial(e))  
    # Saída: 120

# Há mais funções matemáticas na bliblioteca, principalmente para verificação de número, como; é infinito? é um número? gdc() que retorna uma MDC, entre outros
#!/usr/bin/env python3
# script_temp.py
# conversão de lista de temperaturas em Celsius para Fahrenheit

# usuário insere as temperaturas em Celsius, separadas por espaço
temp_celsius = input("Digite as temperaturas em graus Celsius - separadas por espaço:")

# divide a string digitada em uma lista de elementos, separando pelos espaços 
celsius_lista = temp_celsius.split()

# criando uma lista vazia onde serão armazenadas as temperaturas em Fahrenheit
fahrenheit_lista = []

# verificação de que o usuário inseriu na lista de celsius apenas números válidos
valido = True
for temp in celsius_lista:
    # converte cada elemento da lista para float
    try:
        float(temp)
    except ValueError:
        valido = False 
        break 

if not valido:
    print("Erro: todas as entradas devem ser números!")
else:
    # Cabeçalho da tabela
    print("Celsius   Fahrenheit")
    print("--------------------")

# Converte cada temperatura e imprime o resultado
    for temp in celsius_lista:
        c = float(temp)  # converte para número
        f = (9/5) * c + 32  # fórmula de conversão de celsius em fahrenheit
        fahrenheit_lista.append(f)  # adiciona à lista de Fahrenheit
        print(f"{c:>7}   {f:>10.1f}")  # imprime com formatação em colunas, com uma casa decimal para Fahrenheit

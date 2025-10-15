#!/usr/bin/env python3
# script_CDS.py
# Exercício 05 - avaliação da disciplina

import sys

# 01. Conferir o número de argumentos
if len(sys.argv) != 8: # se for diferente dos 6 números mais 1 sequência ele imprime:
    print("Atenção! Erro, o uso correto é: python3 script_CDS.py <sequência_DNA> n1 n2 n3 n4 n5 n6")
    sys.exit(1) #encerra o programa - não precisa de else

# 02. Armazenando os argumentos em variáveis
seq_dna = sys.argv[1]
coord1 = sys.argv[2:] #lista com seis números (do dois para frente)

# 03. Conferindo se todos os argumentos de posição são números inteiros
if not all(coord.isdigit() for coord in coord1):
    print("Atenção! Erro, as coordenadas n1 a n6 devem ser números inteiros e positivos")
    sys.exit(1)

# 04. Converte os argumentos para inteiros individuais
n1, n2, n3, n4, n5, n6 = map(int, coord1)

# 05. Verifica se o número faz sentido, se ele não é maior que o tamanho da sequência
if any(n > len(seq_dna) for n in [n1, n2, n3, n4, n5, n6]):
    print("Atenção! Erro, uma ou mais coordenadas excedem o tamanho da sequência de DNA.")
    sys.exit(1)

# 06. Extraindo a CDS e os íntrons
CDS1 = seq_dna[n1-1:n2-1]
intron1 = seq_dna[n2-1:n3-1]
CDS2 = seq_dna[n3-1:n4-1]
intron2 = seq_dna[n4-1:n5-1]
CDS3 = seq_dna[n5-1:n6-1]

# 07. Verificando as bases de início e fim dos íntrons
if intron1.startswith("GT") and intron1.endswith("AG"):
        print("Intron1 válido:", intron1)
else:
        print("Intron1 inválido:", intron1)

if intron2.startswith("GT") and intron2.endswith("AG"):
        print("Intron2 válido:", intron2)
else:
        print("Intron2 inválido:", intron2)

# 08. Sequência final
if (intron1.startswith("GT") and intron1.endswith("AG") and
    intron2.startswith("GT") and intron2.endswith("AG")):

    seq_final = CDS1 + CDS2 + CDS3
    print("Os íntrons 1 e 2 são válidos! (GT......AG)")
    print("A sequência final da CDS é:", seq_final)

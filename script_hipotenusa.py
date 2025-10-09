# Script usando argumentos de linha de comando
# script_argv.py
import sys

# Garantindo que o usuário inseriu o nome do script e os dois argumentos esperados
if len(sys.argv) != 3: #se a quantidade for diferente de 3
    print("Atenção! Uso correto: python3 script_argv.py <a> <b>")
    sys.exit(1)

# Guarda os argumentos em variáveis string e verifica se os caracteres da string são dígitos
a_str = sys.argv[1]
b_str = sys.argv[2]

if not (a_str.isdigit() and b_str.isdigit()): #se não for dígito, imprime:
    print("Erro! Os valores devem ser inteiros positivos")
    sys.exit(1)

# Converte as strings em números inteiros
a = int(a_str) 
b = int(b_str)

# Garantindo que os valores são positivos e menores do que 500
if not (0 < a < 500 and 0 < b < 500):
    print("Erro! Ambos os valores devem ser positivos e menores que 500.")
    sys.exit(1)

# Cálculo do quadrado da hipotenusa 
hipotenusa2 = a**2 + b**2

# Impressão da mensagem final 
print(f"O quadrado da hipotenusa para o triângulo com lados A={a} e B={b} é {hipotenusa2}")


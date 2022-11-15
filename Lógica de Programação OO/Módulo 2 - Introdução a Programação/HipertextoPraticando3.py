'''
Problema: Desenvolva um programa que só deve aceitar números pares. Siga as seguintes instruções:
    - Caso um número ímpar seja digitado, informe ao usuário que ele digitou um valor ímpar e peça novamente por um número par;
    - Caso uma letra seja digitada, informe ao usuário que ele digitou um caractere inválido e peça novamente por um número par.
'''

try:
    numero = input("Digite seu número par: ")
    if int(numero) % 2 == 0:
        print(f"O número {numero} é par.")
except:
    print(f"O caractere {numero} é inválido.")

if int(numero) % 2 != 0:
    raise Exception(f"O número {numero} não é par.")
    print("teste")
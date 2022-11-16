'''
Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário
e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.
'''

def programa(): 
    nome = input("Digite seu nome completo: ")
    anoNascimento = input("Digite seu ano de nascimento: ")

    try:
        if int(anoNascimento) < 1922 or int(anoNascimento) > 2021:
            print("O valor inserido é inválido, tente colocar uma ano válido, entre 1922 e 2021. Tente novamente!")
            programa()
        else:
            idade = 2022 - int(anoNascimento)
            print(f"O nome é: {nome}")
            print(f"Sua idade é: {idade}")
    except:
        print(f"Os caracteres '{anoNascimento}' não são válidos, tente novamente!")
        programa()

programa()
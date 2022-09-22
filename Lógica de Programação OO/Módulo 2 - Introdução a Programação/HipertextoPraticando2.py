'''
Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal.
Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², crie um programa que calcule e
informe a classificação do IMC.
'''

def imc(peso, altura):
    imc = peso / (altura*altura)
    return imc

p = float(input("Informe seu peso: "))
a = float(input("Informe sua altura: "))

print(imc(p, a))
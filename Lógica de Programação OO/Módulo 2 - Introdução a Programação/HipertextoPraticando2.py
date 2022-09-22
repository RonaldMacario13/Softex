'''
Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal.
Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², crie um programa que calcule e
informe a classificação do IMC.
'''

def imc(peso, altura):
    imc = peso / (altura*altura)
    if imc <= 18.5:
        return "Magreza"
    elif (imc > 18.5) and (imc <= 24.9):
        return "Saudável"
    elif (imc > 24.9) and (imc <= 29.9):
        return "Sobrepeso"
    elif (imc > 29.9) and (imc <= 39.9):
        return "Obesidade"
    else:
        return "Obesidade grave"

p = float(input("Informe seu peso (em kg): "))
a = float(input("Informe sua altura (em metros): "))

print(imc(p, a))
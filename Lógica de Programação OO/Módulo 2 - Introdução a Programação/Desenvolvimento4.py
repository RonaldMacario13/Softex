'''
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão
os números da operação e o terceiro será a entrada que definirá a operação a ser executada.
Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.
'''

number1 = float(input("Digite o primeiro número: "))
number2 = float(input("Digite o segundo número: "))
ope = float(input("Digite a operação número: "))

def calculadora(number1, ope, number2):
    if 4 >= ope >= 1:
        print({
            1 : (number1 + number2),
            2 : number1 - number2,
            3 : number1 * number2,
            4 : number1 / number2,
            }[ope])
    else:
        print(0)

calculadora(number1, ope, number2)
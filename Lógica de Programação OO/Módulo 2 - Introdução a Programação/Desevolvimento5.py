def calculadora(number1, ope, number2):
    if 4 >= ope >= 1:
        print({
            1 : f"A resposta é {number1 + number2}",
            2 : f"A resposta é {number1 - number2}",
            3 : f"A resposta é {number1 * number2}",
            4 : f"A resposta é {number1 / number2}",
            }[ope])
    else:
        print("Essa opção não existe")

sair = 1
while sair != 0:
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    number1 = float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o segundo número: "))
    ope = float(input("Digite a operação número: "))
    calculadora(number1, ope, number2)
    sair = int(input("Deseja sair? "))
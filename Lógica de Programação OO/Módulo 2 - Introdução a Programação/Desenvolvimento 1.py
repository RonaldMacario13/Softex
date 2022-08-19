'''
Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve.
Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado.
'''

nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite primera nota: "))
nota2 = float(input("Digite segunda nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

media = (nota1 + nota2) / 2

if (media < 7.0) or (faltas > 3):
    print(f"O nome do aluno é: {nome}")
    print("Aluno reprovado!")
else:
    print(f"O nome do aluno é: {nome}")
    print("Aluno Aprovado!")
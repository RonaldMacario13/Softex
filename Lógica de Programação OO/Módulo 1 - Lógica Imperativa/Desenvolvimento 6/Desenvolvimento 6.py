import pandas as pd

# Eu criei um banco de dados para que não seja necessário fazer o input de 100 alunos todas as vezes.
# O csv com os dados está no repositório.

# O delimiter é o delimitador das colunas.
# O index_col coloca as colunas como index.
bancoDeDados = pd.read_csv("bd-Desen6.csv", delimiter=";", index_col=0)

# Mostrar informções do Banco de Dados
# print(bancoDeDados.info())

contadorGeral = 0
contadorA = 0
contadorB = 0
contadorC = 0
contadorD = 0
maiorNota = 0
alunoMaiorNota = 0
turmaMaiorNota = 0
maiorNotaA = 0
maiorNotaB = 0
maiorNotaC = 0
maiorNotaD = 0

for linha in bancoDeDados.itertuples():
    if linha[1] >= 7.0:
        if linha[2] == "A":
            # print(linha[2])
            contadorA += 1
            if linha[1] > maiorNotaA:
                maiorNotaA = linha[1]
        elif linha[2] == "B":
            # print(linha[2])
            contadorB += 1
            if linha[1] > maiorNotaB:
                maiorNotaB = linha[1]
        elif linha[2] == "C":
            # print(linha[2])
            contadorC += 1
            if linha[1] > maiorNotaC:
                maiorNotaC = linha[1]
        else:
            # print(linha[2])
            contadorD += 1
            if linha[1] > maiorNotaD:
                maiorNotaD = linha[1]
        # print(linha[1])
        contadorGeral += 1
    if linha[1] > maiorNota:
        maiorNota = linha[1]
        turmaMaiorNota = linha[2]
        alunoMaiorNota = linha[0]


print(f"Se formaram {contadorGeral} estudantes!")

# Quantos alunos formados em cada turma?
print(f"{contadorA} estudantes da turma A se formaram!")
print(f"{contadorB} estudantes da turma B se formaram!")
print(f"{contadorC} estudantes da turma C se formaram!")
print(f"{contadorD} estudantes da turma D se formaram!")
print("---------------------")

# Qual aluno teve a maior nota e em qual turma?
print(
    f"O aluno que obteve a maior foi {alunoMaiorNota}, da turma {turmaMaiorNota}. A nota dele foi: {maiorNota}!")
print("---------------------")

# Qual a maior nota em cada turma?
print(f"A nota {maiorNotaA} foi a maior da turma A!")
print(f"A nota {maiorNotaB} foi a maior da turma B!")
print(f"A nota {maiorNotaC} foi a maior da turma C!")
print(f"A nota {maiorNotaD} foi a maior da turma D!")

quantRodas = int(input("Qual a quantidade de rodas do veículo? "))
peso = float(input("Qual o peso, em kg, do veículo? "))
quantPessoas = int(input("Qual a quantidade de pessoas que o veículo pode acomodar? "))

# A: Veículos com duas ou três rodas;
# B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
# C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
# D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
# E: Veículos com quatro rodas ou mais e com mais de 6000 kg.

if quantRodas == 2 or quantRodas == 3:
    print("A melhor categoria de habilitação, para o veívulo informado, é: A")
elif quantRodas >= 4:
    if quantRodas == 4 and quantPessoas <= 8 and peso <= 3500:
        print(f"A melhor categoria de habilitação, para o veívulo informado, é: B")
    elif quantRodas >= 4 and quantPessoas <= 8 and 6000 > peso > 3500:
        print(f"A melhor categoria de habilitação, para o veívulo informado, é: C")
    elif quantRodas >= 4 and quantPessoas > 8:
        print(f"A melhor categoria de habilitação, para o veívulo informado, é: D")
    elif quantRodas >= 4 and quantPessoas <= 8 and peso > 6000:
        print(f"A melhor categoria de habilitação, para o veívulo informado, é: E")
else:
    print("Veículo inválido!")


'''
if quantRodas == 2 or quantRodas == 3:
    print("A melhor categoria de habilitação, para o veívulo informado, é: A")
elif quantRodas == 4 and quantPessoas <= 8 and peso <= 3500:
    print(f"A melhor categoria de habilitação, para o veívulo informado, é: B")
elif quantRodas >= 4 and 6000 > peso > 3500:
    print(f"A melhor categoria de habilitação, para o veívulo informado, é: C")
elif quantRodas >= 4 and quantPessoas > 8:
    print(f"A melhor categoria de habilitação, para o veívulo informado, é: D")
elif quantRodas >= 4 or peso > 6000:
    print(f"A melhor categoria de habilitação, para o veívulo informado, é: E")
else:
    print("Veículo inválido.")
'''
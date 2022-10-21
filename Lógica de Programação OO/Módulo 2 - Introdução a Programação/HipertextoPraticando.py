# import time

# contador = 0
# array = 44 *["_"]

# print("Iniciando contagem!")

# for i in range(1,46):
#     result = [''.join(array)]
#     print(f"{result} {i}/45 sec")
#     if contador < 44:
#         array[contador] = "|"
#     contador += 1
#     time.sleep(1)

# print("Acabou o tempo de descanço!")

import getpass 

#--------Jogo de adivinha-----------#

palavra_secreta = getpass.getpass('Digite a palavra secreta: ')
adivinhar_palavra = input("Digite a palavra: ")

contador = 0

for i in palavra_secreta:
    contador += 1

while palavra_secreta != adivinhar_palavra and contador > 1:
    if palavra_secreta == adivinhar_palavra:
        print("Parabens!")
    else:
         contador = contador - 1
         adivinhar_palavra = input('Voce so tem {0} tentativas, tente novamente: '.format(contador))
if contador == 1:
    print("Voce exedeu a quantidade de tentativas!")
else:
    print("Parabens!")
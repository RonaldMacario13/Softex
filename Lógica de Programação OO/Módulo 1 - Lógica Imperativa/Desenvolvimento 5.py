import unicodedata

# Para entender esse código é necessário abrir a imagem "IlustraçaoDesenvolvimento5".

# A função abaixo está formatando todas as palavras com acentos, para elas ficarem sem acentos.


def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()

# =====================================================
# =====================================================

# A função abaixo está na terceira/quarta parte. Ela acontece se "É pesado" for escolhido. Ela entrega uma resposta.


def pesado():
    print("-----------------------------------------")
    print(" ")
    print('É um Trator!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        pesado()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Tem pedal" for escolhido. Ela entrega uma resposta.


def pedal():
    print("-----------------------------------------")
    print(" ")
    print('É uma Bicicleta!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        pedal()

# A função abaixo está na segunda parte. Ela acontece se "Cabe apenas uma pessoa" for escolhido.


def umaPessoa():
    print("-----------------------------------------")
    print(" ")
    print('"Cabe apenas uma pessoa" foi escolhido!')
    print("Agora quero saber se é pesado ou tem pedal.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É pesado? ").rstrip().lstrip()))
    if resposta == "sim":
        pesado()
    elif resposta == "nao":
        print("Então tem pedal!")
        pedal()
    else:
        print("Resposta inválida! Tente novamente")
        umaPessoa()

# A função abaixo está na segunda parte. Ela acontece se "Usa capacete" for escolhido.


def capacete():
    print("-----------------------------------------")
    print(" ")
    print('É uma moto!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        capacete()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Usa trilho" for escolhido. Ela entrega uma resposta.


def trilho():
    print("-----------------------------------------")
    print(" ")
    print('É um trem!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        trilho()

# A função abaixo está na quarta/quinta parte. Ela acontece se "Usa carroceria" for escolhido. Ela entrega uma resposta.


def carroceria():
    print("-----------------------------------------")
    print(" ")
    print('É um caminhão!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        carroceria()

# A função abaixo está na quinta/sexta parte. Ela acontece se "Pode ter cobrador" for escolhido. Ela entrega uma resposta.


def cobrador():
    print("-----------------------------------------")
    print(" ")
    print('É um ônibus!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        cobrador()

# A função abaixo está na quarta parte. Ela acontece se "É alto" for escolhido.


def altoTerrestre():
    print("-----------------------------------------")
    print(" ")
    print('"É alto" foi escolhido!')
    print("Agora quero saber se usa carroceria ou se pode ter cobrador.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("Usa carroceria? ").rstrip().lstrip()))
    if resposta == "sim":
        carroceria()
    elif resposta == "nao":
        print("Então pode ter cobrador!")
        cobrador()
    else:
        print("Resposta inválida! Tente novamente")
        altoTerrestre()

# A função abaixo está na quarta/quinta parte. Ela acontece se "Veículo leve" for escolhido. Ela entrega uma resposta.


def leve():
    print("-----------------------------------------")
    print(" ")
    print('É um carro!')
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        leve()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Anda na pista" for escolhido.


def pista():
    print("-----------------------------------------")
    print(" ")
    print('"Anda na pista" foi escolhido!')
    print("Agora quero saber se é alto ou é leve.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É alto? ").rstrip().lstrip()))
    if resposta == "sim":
        altoTerrestre()
    elif resposta == "nao":
        print("Então é leve!")
        leve()
    else:
        print("Resposta inválida! Tente novamente")
        pista()


# A função abaixo está na segunda parte. Ela acontece se "Tem passageiro" for escolhido.


def passageiros():
    print("-----------------------------------------")
    print(" ")
    print('"Tem passageiro" foi escolhido!')
    print("Agora quero saber se usa trilho ou anda na pista.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("Usa trilho? ").rstrip().lstrip()))
    if resposta == "sim":
        trilho()
    elif resposta == "nao":
        print("Então anda na pista!")
        pista()
    else:
        print("Resposta inválida! Tente novamente")
        passageiros()

# A função abaixo está na primeira parte. Ela acontece se "Terreste" for escolhido.


def terrestre():
    print("-----------------------------------------")
    print(" ")
    print('"Terrestre" foi escolhido!')
    print("Agora quero saber se cabe apenas uma pessoa, usa capacete ou tem passageiro.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("Cabe apenas uma pessoa? ").rstrip().lstrip()))
    if resposta == "sim":
        umaPessoa()
    elif resposta == "nao":
        resposta = remove_non_ascii_normalized(
            str(input("Usa capacete? ").rstrip().lstrip()))
        if resposta == "sim":
            capacete()
        elif resposta == "nao":
            print("Então tem passageiros!")
            passageiros()
        else:
            print("Resposta inválida! Tente novamente")
            terrestre()
    else:
        print("Resposta inválida! Tente novamente")
        terrestre()

# =====================================================
# =====================================================

# A função abaixo está na segunda/Terceira parte. Ela acontece se "Precisa pular" for escolhido. Ela entrega uma  resposta.


def asaDelta():
    print("-----------------------------------------")
    print(" ")
    print("É uma Asa Delta!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        asaDelta()

# A função abaixo está na terceira/quarta parte. Ela acontece se "É devagar" for escolhido. Ela entrega uma  resposta.


def devagar():
    print("-----------------------------------------")
    print(" ")
    print("É um balão!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        devagar()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Possui asas fixas" for escolhido. Ela entrega uma  resposta.


def asas():
    print("-----------------------------------------")
    print(" ")
    print("É um avião!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        asas()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Faz voo vertical" for escolhido. Ela entrega uma  resposta.


def vertical():
    print("-----------------------------------------")
    print(" ")
    print("É um helicóptero!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        vertical()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Tem piloto" for escolhido.


def piloto():
    print("-----------------------------------------")
    print(" ")
    print('"Tem piloto" foi escolhido!')
    print("Agora quero saber se possui asas fixas ou faz voo vertical.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("Possui asas fixas? ").rstrip().lstrip()))
    if resposta == "sim":
        asas()
    elif resposta == "nao":
        print("Então faz voo vertical!")
        vertical()
    else:
        print("Resposta inválida! Tente novamente")
        piloto()

# A função abaixo está na segunda parte. Ela acontece se "Viaja dentro" for escolhido.


def viajaDentro():
    print("-----------------------------------------")
    print(" ")
    print('"Viaja dentro" foi escolhido.')
    print("Agora quero saber se é devagar ou tem piloto.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É devagar? ").rstrip().lstrip()))
    if resposta == "sim":
        devagar()
    elif resposta == "nao":
        print('Então tem piloto!')
        piloto()
    else:
        print("Resposta inválida! Tente novamente")
        viajaDentro()

# A função abaixo está na primeira parte. Ela acontece se "Aéreo" for escolhido.


def aereo():
    print("-----------------------------------------")
    print(" ")
    print('"Aéreo" foi escolhido!')
    print("Agora quero saber se precisa pular ou viaja dentro.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É preciso pular? ").rstrip().lstrip()))
    if resposta == "sim":
        asaDelta()
    elif resposta == "nao":
        print("Então viaja dentro!")
        viajaDentro()
    else:
        print("Resposta inválida! Tente novamente")
        aereo()

# =====================================================
# =====================================================

# A função abaixo está na segunda / terceira parte. Ela acontece se "É coberto d'água" for escolhido. Ela entrega uma resposta.


def cobertoAgua():
    print("-----------------------------------------")
    print(" ")
    print("É um submarino!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        cobertoAgua()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Possui vela" for escolhido. Ela entrega uma resposta.


def vela():
    print("-----------------------------------------")
    print(" ")
    print("É um barco!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        vela()

# A função abaixo está na quarta/quinta parte. Ela acontece se "É alto" for escolhido. Ela entrega uma resposta.


def altoAquatico():
    print("-----------------------------------------")
    print(" ")
    print("É um navio!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        altoAquatico()

# A função abaixo está na quarta/quinta parte. Ela acontece se "Pode ser descoberto" for escolhido. Ela entrega uma resposta.


def descoberto():
    print("-----------------------------------------")
    print(" ")
    print("É um lancha!")
    tentarNovamente = remove_non_ascii_normalized(
        str(input("Tentar novamente? ").rstrip().lstrip()))
    if tentarNovamente == "sim":
        print("-----------------------------------------")
        print(" ")
        etapa1()
    elif tentarNovamente == "nao":
        print("Obrigado por jogar!")
        exit()
    else:
        print("Resposta inválida, tente novamente!")
        descoberto()

# A função abaixo está na terceira/quarta parte. Ela acontece se "Tem motor" for escolhido.


def motor():
    print("-----------------------------------------")
    print(" ")
    print('"Tem motor" foi escolhido!')
    print("Agora preciso saber se é alto ou pode ser descoberto.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É alto? ").rstrip().lstrip()))
    if resposta == "sim":
        altoAquatico()
    elif resposta == "nao":
        print("Então pode ser descoberto!")
        descoberto()
    else:
        print("Resposta inválida! Tente novamente")
        motor()

# A função abaixo está na segunda parte. Ela acontece se "Navega na água" for escolhido.


def navegaAgua():
    print("-----------------------------------------")
    print(" ")
    print('"Navega na água" foi escolhido!')
    print("Agora preciso saber se possuí vela ou tem motor.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("Possuí vela? ").rstrip().lstrip()))
    if resposta == "sim":
        vela()
    elif resposta == "nao":
        print("Então tem motor!")
        motor()
    else:
        print("Resposta inválida! Tente novamente")
        navegaAgua()

# A função abaixo está na primeira parte. Ela acontece se "É aquático" for escolhido.


def aquatico():
    print("-----------------------------------------")
    print(" ")
    print('"Aquático" foi escolhido!')
    print("Agora quero saber se é coberto d'água ou Navega na água.")
    global resposta
    resposta = remove_non_ascii_normalized(
        str(input("É coberto d'água? ").rstrip().lstrip()))
    if resposta == "sim":
        cobertoAgua()
    elif resposta == "nao":
        print("Então navega na água!")
        navegaAgua()
    else:
        print("Resposta inválida! Tente novamente")
        aquatico()

# =====================================================
# =====================================================

# A função abaixo inicia todo o programa. Ele faz as primeiras perguntas.


def etapa1():
    global categoria
    print("Olá, vou descobrir qual meio de transporte você está pensando!")
    print("Primeiro quero saber se ele é terrestre, aéreo ou aquático.")
    print('Responda com "sim" ou "não".')
    categoria = remove_non_ascii_normalized(
        str(input("É terrestre? ").rstrip().lstrip()))
    if categoria == "sim":
        terrestre()
    elif categoria == "nao":
        categoria = remove_non_ascii_normalized(
            str(input("É aéreo? ").rstrip().lstrip()))
        if categoria == "sim":
            aereo()
        elif categoria == "nao":
            print("Então seu carro é aquático!")
            aquatico()
        else:
            print("Resposta inválida! Tente novamente")
            etapa1()
    else:
        print("Resposta inválida! Tente novamente")
        etapa1()


etapa1()

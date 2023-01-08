pontRonald = 0
pontAna = 0
pontDavide = 0
branco = 0
nulo = 0
repeticao = True
pontMaior = 0
vencedor = ""

def separador():
    print("")
    print("----------------------")

def votacao():
    global pontRonald
    global pontAna
    global pontDavide
    global branco
    global nulo
    print("Bem-vindo à votação!")
    separador()
    print("Os candidatos são:\nRônald = 889\nAna Rosa = 847\nDávide = 515")
    separador()
    try:
        resposta = int(input("Digite seu voto: "))
        if resposta == 889:
            print("Voto para Rônald!")
            separador()
            pontRonald += 1
        elif resposta == 847:
            print("Voto para Ana Rosa!")
            separador()
            pontAna += 1
        elif resposta == 515:
            print("Voto para Dávide!")
            separador()
            pontDavide += 1
        elif resposta == 0:
            print("Voto branco!")
            separador()
            branco += 1
        else:
            print("Voto nulo!")
            separador()
            nulo += 1
    except:
        print("Digite um número inteiro. Tente novamente.")
        separador()
        votacao()

def finalizar():
    global repeticao
    print("Deseja finalizar a votação?")
    rep = str(input("Digite sua resposta com 'sim' ou 'não': "))
    if rep == "sim" or rep == "Sim":
        repeticao = False
    elif rep == "não" or rep == "Não" or rep == "nao" or rep == "Nao":
        repeticao = True
    else:
        print("Resposta inválida, tente novamente.")
        finalizar()

def comparador():
    global pontMaior 
    global vencedor
    contador = -1
    pontuacoes = [pontRonald, pontAna, pontDavide, branco, nulo]
    dicio = {0: "Rônald", 1: "Ana Rosa", 2: "Dávide", 3: "Branco", 4: "Nulo"}

    pontMaior = max(pontuacoes)
    for n in  pontuacoes:
        contador += 1
        if pontMaior == n:
            vencedor = dicio[contador]

def sistema():
    global vencedor
    global pontMaior
    while repeticao:
        votacao()
            
        finalizar()

    comparador()
    separador()
    print("Votação encerrada!")
    print("")
    print(f"O vencedor foi {vencedor}, com a pontuação de {pontMaior}")
    separador()
    print("Pontuações:")
    print(f"Rônald = {pontRonald}")
    print(f"Ana Rosa = {pontAna}")
    print(f"Dávide = {pontDavide}")
    print(f"Brancos = {branco}")
    print(f"Nulos = {nulo}")

sistema()
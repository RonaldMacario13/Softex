'''
import unicodedata

def remove_non_ascii_normalized(string: str) -> str:
    normalized = unicodedata.normalize('NFD', string)
    return normalized.encode('ascii', 'ignore').decode('utf8').casefold()
'''


def inicio():
    print("Olá, vamos descobrir qual meio de transporte você está pensando!")
    print("É terrestre, aéreo ou aquático?")
    global categoria
    categoria = str(
        input('Digite "1" para terrestre, "2" para aéreo e "3" para aquático: '))

    if categoria == "1":
        print("Terrestre foi escolhido.")

    elif categoria == "2":
        print("Aéreo foi escolhido.")

    elif categoria == "3":
        print("Aquático foi escolhido.")

    else:
        print("Resposta inválida! Tente novamente.")
        inicio()

    return categoria
# ===============================================================
# ===============================================================


def terrestre():
    print("Cabe apenas uma pessoa, usa capacete ou tem passageiro?")
# ===============================================================
# ===============================================================


def aereo():

    # ===============================================================
    # ===============================================================


def aquatico():

    # ===============================================================
    # ===============================================================


def etapa2():
    if categoria == "1":
        terrestre()
    elif categoria == "2":
        aereo()
    else:
        aquatico()


categoria = inicio()
print(categoria)

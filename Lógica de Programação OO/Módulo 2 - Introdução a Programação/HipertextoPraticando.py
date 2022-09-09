import time

contador = 0
array = 44 *["_"]

print("Iniciando contagem!")

for i in range(1,46):
    result = [''.join(array)]
    print(f"{result} {i}/45 sec")
    if contador < 44:
        array[contador] = "|"
    contador += 1
    time.sleep(1)

print("Acabou o tempo de descanço!")

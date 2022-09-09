import time

contador = 10
array = 10 *["|"]

print("iniciando contagem regressiva")

for i in range(10, 0, -1):
    result = [''.join(array)]
    print(f"{result} {i}/10 sec")
    contador -= 1
    if contador < 10:
        array[contador] = "_"
    time.sleep(1)

print("BUM!")
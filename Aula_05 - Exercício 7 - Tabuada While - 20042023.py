print("Tabuada")
numero = int(input("Entre com o numero da tabuada "))
i = 1
while i <= 10 :
    tabuada = numero * i
    print(f'{numero} X {i} = {tabuada}')
    i = i + 1

print("Tabuada com comandos curtos")
i = 1
while i <= 10 :
    print(f'{numero} X {i} = {numero * i}')
    i += 1
# Crie um algoritmo que simule um 
# temporizador. Peça os minutos e imprima um relógio de minutos e segundos. 
# Utilize o FOR – um for dentro do outro 

print("Temporizador")
minutos = int(input("Entre com os minutos"))

print(f'{minutos:02d}:00')

while minutos > 0:
    minutos = minutos - 1
    segundos = 60
    while segundos > 0:
        segundos = segundos -1
        print(f'{minutos:02d}:{segundos:02d}')
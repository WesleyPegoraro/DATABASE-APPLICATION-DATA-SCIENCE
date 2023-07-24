# Faça um programa que solicite 4 números ao usuário e ao final exiba os 4 números
# em ordem crescente.

print("Ordenacao")

a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))
d = int(input("Entre com o quarto número: "))

# Essa formatação é mais antiga, posicional.
# O d significa decimal (para inteiros), o f para float, o s para string
# print('Os numeros originais sao %d %d %d %d'%(a, b, c, d))

print(f'Os números digitados foram: {a} {b} {c} {d}')
if a > b:
    aux = b
    b = a
    a = aux
# print(f'{a} {b} {c} {d}')
if a > c:
    aux = c
    c = a
    a = aux
# print(f'{a} {b} {c} {d}')
if a > d:
    aux = d
    d = a
    a = aux
# print(f'{a} {b} {c} {d}')
if b > c:
    aux = c
    c = b
    b = aux
# print(f'{a} {b} {c} {d}')
if b > d:
    aux = d
    d = b
    b = aux
# print(f'{a} {b} {c} {d}')
if c > d:
    aux = d
    d = c
    c = aux
print(f'Os numeros em ordem são: {a} {b} {c} {d}')
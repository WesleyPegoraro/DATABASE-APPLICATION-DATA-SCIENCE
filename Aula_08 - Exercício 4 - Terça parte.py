# Crie um algoritmo que solicite 10 números e imprima a terça parte deles.
# Utilize o FOR, atenção a formatação.

titulo = "a terça parte".capitalize()
print(f'{titulo:^30}')
# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = round(numero / 3, 2)
#     print(f'A terça parte de {numero} é {total}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     print(f'A terça parte de {numero} é {round(numero / 3, 2)}')

# for i in range(3):
#     numero = int(input("Entre com um numero"))
#     total = numero / 3
#     print(f'A terça parte de {numero} é {total:.2f}')
#
for i in range(3):
    print(f'A terça parte do numero é {int(input("Entre com um numero"))/3}')
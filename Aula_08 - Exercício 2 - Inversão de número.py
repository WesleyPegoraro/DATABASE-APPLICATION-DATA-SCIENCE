# Crie um algoritmo que peça um 
# número de 4 dígitos e inverta esses dígitos. Exemplo: o número 3578 deverá 
# ser impresso 8753

print("Inversao de Numero")
numero = int(input("Entre com um numero de 4 digitos:"))
# #Alcides way of live
# print(numero)
# print(type(numero))
# numero_invertido = numero[::-1]
# print(type(numero_invertido))
# print(numero_invertido)

# dig4   dig3   dig2   dig1
# milhar centena dezena unidade
# 3      7       5       8

# resultado esperado
# unidade dezena centena milhar
# 8        5      7       3

# se eu dividir um numero por 10 (divisao inteira) o resto vai ser sempre a UNIDADE
# numero = 3758
#
# print("Numero original",numero)
# dig1 = numero % 10
# print("Digito1", dig1)
# numero = numero // 10
# print("Novo Numero:", numero)
#
# dig2 = numero % 10
# print("Digito2", dig2)
# numero = numero// 10
# print("Novo Numero 1:", numero)
#
# dig3 = numero % 10
# print("Digito3", dig3)
# numero = numero // 10
# print("Novo Numero 2:", numero)
#
# numero_novo_final = int(str(dig1) + str(dig2) + str(dig3) + str(numero))
# print(numero_novo_final)

# transformando em repeticao
#numero = 3758
numero_invertido = ""
while(numero > 0):
    dig = numero % 10
    numero_invertido = numero_invertido + str(dig)
    print(numero_invertido)
    numero = numero // 10

print("Final", numero_invertido)
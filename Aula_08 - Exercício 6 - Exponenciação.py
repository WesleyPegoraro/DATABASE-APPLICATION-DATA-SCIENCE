x = int(input('numero a ser exponenciado: ')) 
y = int(input('quantidade a ser exponenciada: ')) 
 
#Exemplo x =3 e y =4    3*4 = 3 x 3 x 3 x 3 
conta = 1 #numero neutro da multiplicação 
if x > 1 and y >= 2:
    for i in range(y): 
        conta = conta + x 
        print(f'conta {i}:', conta) 
else: 
    print('Numeros invalidos')
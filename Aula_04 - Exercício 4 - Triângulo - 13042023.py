print("Triangulo")
a = float(input("Entre com a medida do lado A "))
b = float(input("Entre com a medida do lado B "))
c = float(input("Entre com a medida do lado C "))

#if a > 0 and b > 0 and c > 0:
#verificado que é um triangulo
if a < b + c or b < a + c or c < a + b:
    if a == b == c: # a==b and b==c
        print("Equilatero")
    elif a==b or a==c or b==c:
        print("Isoceles")
    else:
        print("Escaleno")
else:
    print("Não é um triangulo")

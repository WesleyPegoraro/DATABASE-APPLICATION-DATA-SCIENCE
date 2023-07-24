print("Nota")
nota = float(input("Qual sua nota? "))
if nota >= 0 and nota <= 10:
    if nota >= 6:
        print("Aprovado")
    else:
        if nota >= 4:
            print("Exame")
        else:
            print("Reprovado")
else:
    print("Nota inválida")
print("Adivinhacao")
cor_esperada = 'AmarEla'
cor = input("Qual cor voce pensou? ").lower()
print(cor)
if cor == cor_esperada.lower():
    print("Adivinhou")
else:
    print("Quem pena, pensei em", cor_esperada)
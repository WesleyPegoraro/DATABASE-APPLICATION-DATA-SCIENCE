print("Estacionamento")
custo_hora = 5.00
teto = 35
hora = float(input("Quantas hrs vc ficou estacionado? "))
total = hora * custo_hora
if total >= teto:
    print("Voce deve pagar", teto)
else:
    print("Voce deve pagar", total)
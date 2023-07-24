print("Compras")
preco = float(input("Qual o preco da mercadoria? "))
carteira = float(input("Quantos reais eu tenho na carteira? "))
if carteira >= preco:
  print("Posso comprar pois custa", preco, "e eu tenho", carteira)
else:
  falta = preco - carteira
  print("Preciso economizar pois falta", falta)
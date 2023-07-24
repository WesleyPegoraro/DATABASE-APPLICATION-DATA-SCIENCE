print("Abastecimento")
bloco = int(input("Qual bloco você mora?"))
if (bloco == 1) or (bloco == 3):
  print("Você é abastecido pela caixa B")
else: # isso está errado  (bloco == 2) or (bloco == 4): o comando else NAO ACEITA NOVA COMPARACAO
  print("Você é abastecido pela caixa A")
# Entre com o estado da pessoa e imprima as mensagens:
# carioca, paulista, mineiro, baiano, cearense, outros estados

print("Estados")
estado = input("Entre com a sigla estado: ").upper()
if estado == 'SP':
    print('Paulista')
elif estado == 'RJ':
    print('Carioca')
elif estado == 'BA':
    print('Baiano')
else:
    print("Outros Estados")
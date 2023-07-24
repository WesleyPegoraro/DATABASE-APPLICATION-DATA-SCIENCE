print("CNH - desvio condicional composto - com o else")
idade = int(input("Qual sua idade?"))
if idade >= 18:
  print("Você pode dirigir")
  print("Mas precisa tirar a CNH")
else:
  print("Você ainda não pode dirigir")
print("Esse comando é sempre excutado")
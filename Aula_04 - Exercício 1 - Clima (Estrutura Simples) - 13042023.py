print("Clima - Estrutura Simples")
nuvem = input("Tem nuvem no ceu? ").lower().strip()
frio = input("Esta frio hoje? ").lower().strip()

if nuvem == 'sim' and frio == 'sim':
    print("Vai chover")
else:
    print("Nao chove")
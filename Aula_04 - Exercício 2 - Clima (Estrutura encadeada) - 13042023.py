print("Clima Estrutura Encadeada")
nuvem = input("Tem nuvem no ceu? ").lower().strip()
if nuvem in ('sim', 'yes', 'y', 's', 'si'):
    frio = input("Esta frio hoje? ").lower().strip()
    if frio in ('sim', 'yes', 'y', 's', 'si'):
        print("Vai chover")
    else:
        print("Não Chove")
else:
    print("Nao chove")
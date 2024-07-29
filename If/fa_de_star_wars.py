filme = input("Já assistiu todos os filmes?")
camiseta = input("Tem camiseta temática?")
fantasia = input("Já se fantasiou de algum personagem?")
objeto = input("Tem algum action figure/nave/etc?")
parque = input("Já foi no Galaxy's Edge, o parque temático da franquia?")

contador = 0
if filme == 'sim':
    contador += 1
if camiseta == 'sim':
    contador += 1
if fantasia == 'sim':
    contador += 1
if objeto == 'sim':
    contador += 1
if parque == 'sim':
    contador += 1

if contador == 5:
    print("One with the Force")
elif contador == 3 or contador == 4:
    print("Jedi")
elif contador == 2:
    print("Padawan")
else:
    print("Inocente")

               
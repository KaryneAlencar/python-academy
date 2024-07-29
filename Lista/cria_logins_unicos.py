lista_logins = []
verifica = True
i = 1
while verifica:
    login = input('Digite o loguin: ')
    if login == 'fim':
        break
    if login not in lista_logins:
        lista_logins.append(login)
    else:
        i = 1
        nova_tentariva = f"{login}{i}" #cria uma variável para as derivadas de um login ja existente
        while nova_tentariva in lista_logins:
            i += 1
            nova_tentariva = f"{login}{i}" #atualiza a nova tentativa
        lista_logins.append(nova_tentariva) 
for login in lista_logins:
    print(login)
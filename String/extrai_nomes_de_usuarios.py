def extrai_nomes_de_usuarios(lista_email):
    lista_usuarios  =[]
    for email in lista_email:
        partes = email.split('@') 
        nome = partes[0]
        lista_usuarios.append(nome)
    return lista_usuarios
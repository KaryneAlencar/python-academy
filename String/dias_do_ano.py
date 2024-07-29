def dias_do_ano(data):
    # Tabela fixa para os dias em cada mês em um ano não bissexto
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Dividir a data em dia, mês e ano
    partes = data.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    
    # Calcular o número de dias passados desde o início do ano
    dias_passados = 0
    
    # Adicionar os dias dos meses anteriores
    for i in range(mes - 1):
        dias_passados += dias_por_mes[i]
    
    # Adicionar os dias do mês atual
    dias_passados += dia - 1
    
    return dias_passados

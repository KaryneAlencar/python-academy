def quando_passa(dic_grade, programa_desejado):
    dic_horarios = {}

    for canal, programacao in dic_grade.items():
        for horario, programa in programacao.items():
            if programa == programa_desejado:
                if horario in dic_horarios:
                    dic_horarios[horario].append(canal)
                else:
                    dic_horarios[horario] = [canal]
                
    return dic_horarios


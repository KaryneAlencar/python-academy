def compromisso_no_periodo(grade, dia, periodo):
    if grade[dia][periodo] == '':
        return 'Livre'
    else:
        return grade[dia][periodo]
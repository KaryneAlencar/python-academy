def converteHora(horario):
  # se for 0
    if int(horario[:2]) == 0:
        return f"12{horario[2:]} AM"

  # Se for 12
    if int(horario[:2]) == 12:
        return f"12{horario[2:]} PM"
  
  # Se for de tarde
    if int(horario[:2]) > 12:
    
        return f"0{int(horario[:2]) - 12 }{horario[2:]} PM"

    return f"{horario} AM"
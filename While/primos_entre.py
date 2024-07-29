def primos_entre(a, b):
    contador = 0
    i = a
    while i <= b:
        if i> 1:
            if i == 2 or i == 3:
                contador += 1
            elif i % 2 != 0 and i % 3 != 0:
                primo = True
                j = 5
                while j * j <= i:
                    if i % j == 0:
                        primo = False
                        break
                    j += 2
                if primo:
                    contador += 1
        i += 1

    return contador
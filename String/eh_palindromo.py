def eh_palindromo(string):
    palavra_invertida = string[::-1]
    if string == palavra_invertida:
        return True
    else: 
        return False
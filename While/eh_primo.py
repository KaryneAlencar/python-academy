def eh_primo(n):
    if n == 1 or n <= 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
   
    i = 3
    while i < n:
        if n % i == 0:
            return False
        i += 2
    return True
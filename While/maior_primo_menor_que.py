def primo(n):
    #verifica se o número é primo, retornando true or false
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def maior_primo_menor_que(n):
    #retorna o último primo, ou -1 caso não haja primos
    if n < 0:
        return -1
    while n >= 2:
        if primo(n):
            return n
        n -= 1 #vai subtraindo para encontrar o último primo
    return -1
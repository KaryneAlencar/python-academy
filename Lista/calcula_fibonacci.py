def calcula_fibonacci(n):
    fibonacci = []
    if n == 1:
        fibonacci.append(1)
        return fibonacci
    prox = 0
    term1 = 1
    term2 = 1
    fibonacci.append(term1)
    fibonacci.append(term2)
    i = 3
    while i <= n:
        prox = term1 + term2
        term1 = term2
        term2 = prox
        i += 1
        fibonacci.append(prox)
    return fibonacci 
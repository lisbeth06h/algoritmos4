def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci_memo(n, cache={}):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_memo(n-1, cache) + fibonacci_memo(n-2, cache)
    return cache[n]

print(fibonacci(30))  # Esto puede ser lento para n grandes
print(fibonacci_memo(30))  # Esto es mucho más rápido para n grandes


def cambio(cantidad, moneda):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')  # No es posible hacer el cambio
    minimo = float('inf')
    
    for moneda in monedas:
        resultado = cambio(cantidad - moneda, monedas)
        minimo = min(resultado + 1, minimo)

    return minimo

monedas = [1, 5, 10, 25]
print(cambio(50, monedas))  # Debería devolver 2 (10 +
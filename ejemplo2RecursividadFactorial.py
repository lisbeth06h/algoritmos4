def factorial_recursivo(n):
    resultado = 0
    if n <= 1:
        print("Total: 1")
        return 1
    return n * factorial_recursivo (n-1)
resultado = factorial_recursivo(5)
print("Total: ", resultado)


#"Mejorado"
def factorial_recursivo(n):
    if n <= 1:
        return 1
    return n * factorial_recursivo(n-1)

resultado = factorial_recursivo(5)
print("Total:", resultado)
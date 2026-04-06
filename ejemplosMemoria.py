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





#{[()]}
def verificar_expresion(expresion):
    pila = []

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for caracter in expresion:
        if caracter in "([{":
            pila.append(caracter)

        elif caracter in ")]}":
            if not pila:
                return False
            
            ultimo = pila.pop()

            if pares[caracter] != ultimo:
                return False

    return len(pila) == 0



def infija_a_postfija(expresion):
    precedencia = {
        '+': 1,
        '-': 1, 
        '*': 2, 
        '/': 2
    }
    salida = []
    pila = []

    tokens = expresion.split()

    for token in tokens:
        if token.lstrip('-').replace('.', '', 1).isdigit():  # Verificar si es un número (incluyendo negativos y decimales)
            salida.append(token)
            print(f"{token} (número)-> se añade a la salida.")
        elif token == '(':
            pila.push(token)
            print(f"{token} -> se añade a la pila.")
        elif token == ')':
            while not pila.esta_vacia() and pila.peek() != '(':
                salida.append(pila.pop())
            pila.pop()  # Eliminar el '(' de la pila
            print(f"{token} -> se procesan los operadores hasta encontrar '('.")
        elif token in precedencia:
            while (not pila.esta_vacia() and pila.peek() != '(' and pila.peek() in precedencia and
                 precedencia[pila.peek()] >= precedencia[token]):
                salida.append(pila.pop())
            pila.push(token)
            print(f"{token} (operador) -> se procesa según la precedencia.")
    while not pila.esta_vacia():
        salida.append(pila.pop())
    resultado = ' '.join(salida)
    print(f"Expresión postfija: {resultado}")
    
infija_a_postfija("3 + 4 * 2 ")



def demo_operaciones_basicas():
    print("=" *60)

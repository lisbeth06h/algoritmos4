def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b - 1)

def potencia_optimizado(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        mitad = potencia_optimizado(a, b //2)
        return mitad * mitad
    else:
        return a * potencia_optimizado(a, b - 1)
    
def suma_dijitos(n):
    if n < 10:
        return n
    
    digito = n %10
    return digito + suma_dijitos(n // 10)

def suma_lista_normal(lista):
    if len(lista) == 0:
        return 0
    return lista [0] + suma_lista_normal(lista[1:])

   #otra forma más eficiente con tail
    if len(lista) == 0:
        return acomulador
    return suma_lista_tail(lista[1:], acomulador + lista[0])


#ejemplo potencia
def potencia_normal(base, exp):
    #version normal
    if exp == 0:
        return 1
    return base * potencia_normal(base, exp - 1)

    #otra forma más eficiente con tail
    if exp == 0:
        return acomulador
    return  potencia_normal_tail(lista[1:], acomulador + lista[0])

#Invertir lista
def invertir_normal(lista, acomulador = 1):
    if len(lista) <= 1:
        return lista
    return invertir_normal(lista[1:] + [lista[0]])


   #otra forma más eficiente con tail
    if len(lista) <= 1:
        return acomulador
    return invertir_normal_tail(lista[1:], acomulador + [lista[0]])




"""
Ejercicio 4: Búsqueda Binaria Recursiva
Semana 3 - Algoritmos Recursivos
"""

def busqueda_binaria(lista, objetivo, inicio=0, fin=None):
    """
    Busca un elemento en una lista ORDENADA usando búsqueda binaria.
    
    Algoritmo:
        1. Encontrar el elemento del medio
        2. Si es el objetivo, retornar su índice
        3. Si objetivo < medio, buscar en mitad izquierda
        4. Si objetivo > medio, buscar en mitad derecha
        5. Caso base: inicio > fin → no encontrado (-1)
    
    Args:
        lista: Lista ordenada de elementos
        objetivo: Elemento a buscar
        inicio: Índice inicial del rango de búsqueda
        fin: Índice final del rango de búsqueda
    
    Returns:
        Índice del elemento si se encuentra, -1 si no existe
    """
    # Inicializar fin en la primera llamada
    if fin is None:
        fin = len(lista) - 1
    
    # Caso base: rango inválido (elemento no encontrado)
    if inicio > fin:
        return -1
    
    # Calcular punto medio
    medio = (inicio + fin) // 2
    
    # Comparar y decidir en qué mitad buscar
    if lista[medio] == objetivo:
        return medio  # Encontrado
    elif objetivo < lista[medio]:
        # Buscar en la mitad izquierda
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    else:
        # Buscar en la mitad derecha
        return busqueda_binaria(lista, objetivo, medio + 1, fin)


# ============ PRUEBAS ============
if __name__ == "__main__":
    lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Lista: {lista}\n")
    
    casos = [
        (7, 3),    # Existe, índice 3
        (1, 0),    # Primer elemento
        (19, 9),   # Último elemento
        (10, -1),  # No existe
        (0, -1),   # Menor que todos
        (20, -1),  # Mayor que todos
    ]
    
    for objetivo, esperado in casos:
        resultado = busqueda_binaria(lista, objetivo)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} buscar({objetivo}) = {resultado} (esperado: {esperado})")



"""
Ejercicio 1: Potencia Recursiva
Semana 3 - Algoritmos Recursivos

Implementa una función que calcule base^exponente de forma recursiva.
"""

def potencia(base, exponente):
    """
    Calcula base elevado a exponente de forma recursiva.
    
    Ejemplos:
        potencia(2, 3) = 8
        potencia(5, 0) = 1
        potencia(3, 4) = 81
    
    Caso base: exponente == 0 → retorna 1
    Caso recursivo: base × potencia(base, exponente - 1)
    """
    # Caso base: cualquier número elevado a 0 es 1
    if exponente == 0:
        return 1
    # Caso recursivo: base * base^(exponente-1)
    return base * potencia(base, exponente - 1)


def potencia_optimizada(base, exponente):
    """
    BONUS: Versión optimizada usando la propiedad:
    - Si exponente es par: base^n = (base^(n/2))^2
    - Si exponente es impar: base^n = base × base^(n-1)
    
    Esto reduce la complejidad de O(n) a O(log n)
    """
    # Caso base
    if exponente == 0:
        return 1
    # Si el exponente es par: (base^(n/2))^2
    if exponente % 2 == 0:
        mitad = potencia_optimizada(base, exponente // 2)
        return mitad * mitad
    # Si el exponente es impar: base * base^(n-1)
    else:
        return base * potencia_optimizada(base, exponente - 1)


# ============ PRUEBAS ============
if __name__ == "__main__":
    print("=== Pruebas de potencia ===")
    
    casos = [
        (2, 0, 1),
        (2, 1, 2),
        (2, 3, 8),
        (2, 10, 1024),
        (3, 4, 81),
        (5, 3, 125),
    ]
    
    for base, exp, esperado in casos:
        resultado = potencia(base, exp)
        estado = "✓" if resultado == esperado else "✗"
        print(f"{estado} potencia({base}, {exp}) = {resultado} (esperado: {esperado})")
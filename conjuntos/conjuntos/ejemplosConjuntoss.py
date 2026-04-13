"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL - CONJUNTOS
                    Validador de Sudoku + Sistema de Permisos
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES:
--------------
1. Completar las funciones donde dice TODO
2. No modificar el código base proporcionado


═══════════════════════════════════════════════════════════════════════════════
                            PARTE 1: VALIDADOR DE SUDOKU (3.5)
═══════════════════════════════════════════════════════════════════════════════

Usar conjuntos de Python para validar un tablero de Sudoku.

REGLAS DEL SUDOKU:
- Cada fila debe contener los números 1-9 sin repetir
- Cada columna debe contener los números 1-9 sin repetir
- Cada subcuadro 3x3 debe contener los números 1-9 sin repetir
"""

NUMEROS_VALIDOS = {1, 2, 3, 4, 5, 6, 7, 8, 9}

TABLERO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


# puntO 1.1 — validar una fila
def validar_fila(tablero, num_fila):
    fila = set(tablero[num_fila])
    return fila == NUMEROS_VALIDOS

# PUNTO 1.2 — validar una columna
def validar_columna(tablero, num_columna):
    columna = set(tablero[i][num_columna] for i in range(9))
    return columna == NUMEROS_VALIDOS

# PUNTO 1.3 — validar un subcuadro 3x3
def validar_subcuadro(tablero, fila_inicio, col_inicio):
    numeros = set()
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            numeros.add(tablero[i][j])
    return numeros == NUMEROS_VALIDOS
"""
═══════════════════════════════════════════════════════════════════════════════
                    PARTE 2: SISTEMA DE PERMISOS CON LISTAS (2.0)
═══════════════════════════════════════════════════════════════════════════════

Implementar operaciones de subconjuntos usando la clase Conjunto con listas enlazadas.

CONTEXTO:
Un sistema tiene roles con diferentes permisos. Debes verificar si un rol
tiene todos los permisos necesarios para realizar ciertas acciones.
"""


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO BASE - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)
    
    def esta_vacio(self):
        return self.cabeza is None
    
    def pertenece(self, x):
        """Retorna True si x está en el conjunto"""
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False
    
    def agregar(self, x):
        """Agrega x si no existe"""
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True
    
    
    def __str__(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return "{" + ", ".join(elementos) + "}"


# ═══════════════════════════════════════════════════════════════════════════════
# PUNTOS A IMPLEMENTAR
# ═══════════════════════════════════════════════════════════════════════════════

# PUNTO 2.1 (1.0): Verificar si es subconjunto, si A ⊆ B
def es_subconjunto(d1, d2):
    """
    Retorna True si conjunto_a es subconjunto de conjunto_b.
    Es decir, si TODOS los elementos de A están en B.
    
    A ⊆ B significa: para todo x en A, x también está en B
    
    Ejemplo:
        A = {leer, escribir}
        B = {leer, escribir, eliminar}
        es_subconjunto(A, B) -> True (A ⊆ B)
        es_subconjunto(B, A) -> False (B no es subconjunto de A)
    
    """
    # Recorre cada elemento de d1 y verifica que esté en d2
    actual = d1.cabeza
    while actual:
        if not d2.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True
    
# PUNTO 2.2 (0.5): Verificar permisos de usuario
def tiene_permisos(permisos_usuario, permisos_requeridos):
    """
    Retorna True si el usuario tiene TODOS los permisos requeridos.
    
    Esto es equivalente a verificar si permisos_requeridos ⊆ permisos_usuario
    
    Ejemplo:
        usuario = Conjunto(["leer", "escribir", "eliminar"])
        requeridos = Conjunto(["leer", "escribir"])
        tiene_permisos(usuario, requeridos) -> True
        
        requeridos2 = Conjunto(["leer", "admin"])
        tiene_permisos(usuario, requeridos2) -> False (no tiene "admin")
    """
    
    """Verifica si el usuario tiene todos los permisos necesarios"""



    # TODO: Implementar usando es_subconjunto

    # requeridos ⊆ usuario  →  el usuario tiene todo lo necesario
    return es_subconjunto(permisos_requeridos, permisos_usuario)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("PARTE 1: VALIDADOR DE SUDOKU")
    print("=" * 60)
    
    # Probar validación de filas
    print("\n📋 Validando filas:")
    for i in range(9):
        resultado = validar_fila(TABLERO, i)
        print(f"  Fila {i+1}: {'✓' if resultado else '✗'}")
    
    # Probar validación de columnas
    print("\n📋 Validando columnas:")
    for j in range(9):
        resultado = validar_columna(TABLERO, j)
        print(f"  Columna {j+1}: {'✓' if resultado else '✗'}")
    
    # Probar validación de subcuadros
    print("\n📋 Validando subcuadros 3x3:")
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            resultado = validar_subcuadro(TABLERO, fi, ci)
            print(f"  Subcuadro ({fi+1},{ci+1}): {'✓' if resultado else '✗'}")
    
    print("\n" + "=" * 60)
    print("PARTE 2: SISTEMA DE PERMISOS")
    print("=" * 60)
    
    # Definir roles
    admin = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])
    editor = Conjunto(["leer", "escribir"])
    viewer = Conjunto(["leer"])
    
    print(f"\n👤 Roles definidos:")
    print(f"  Admin: {admin}")
    print(f"  Editor: {editor}")
    print(f"  Viewer: {viewer}")
    
    # Probar subconjuntos
    print(f"\n🔍 Verificando subconjuntos:")
    print(f"  ¿Viewer ⊆ Editor? {es_subconjunto(viewer, editor)}")  # True
    print(f"  ¿Editor ⊆ Admin? {es_subconjunto(editor, admin)}")    # True
    print(f"  ¿Admin ⊆ Editor? {es_subconjunto(admin, editor)}")    # False
    
    # Probar permisos
    print(f"\n🔐 Verificando permisos:")
    
    accion_editar = Conjunto(["leer", "escribir"])
    accion_admin = Conjunto(["crear_usuarios", "eliminar"])
    
    print(f"  Acción editar requiere: {accion_editar}")
    print(f"  Acción admin requiere: {accion_admin}")
    
    print(f"\n  ¿Editor puede editar? {tiene_permisos(editor, accion_editar)}")  # True
    print(f"  ¿Viewer puede editar? {tiene_permisos(viewer, accion_editar)}")    # False
    print(f"  ¿Admin puede hacer acción admin? {tiene_permisos(admin, accion_admin)}")  # True
    print(f"  ¿Editor puede hacer acción admin? {tiene_permisos(editor, accion_admin)}")  # False





    # 1a (1.0 pt): Retorna un nuevo Conjunto con los elementos que están en AMBOS conjuntos
def interseccion(c1, c2):
    """
    Ejemplo:
        A = Conjunto(["leer", "escribir", "admin"])
        B = Conjunto(["leer", "escribir", "eliminar"])
        interseccion(A, B) -> {"leer", "escribir"}
    """
    # TODO
    pass

# 1b (1.0 pt): Retorna un nuevo Conjunto con TODOS los elementos de ambos conjuntos
def union(c1, c2):
    """
    Ejemplo:
        A = Conjunto(["leer", "escribir"])
        B = Conjunto(["escribir", "eliminar"])
        union(A, B) -> {"leer", "escribir", "eliminar"}  (sin repetir)
    """
    # TODO
    pass
# 1c (0.5 pt): Retorna un nuevo Conjunto con los elementos de c1 que NO están en c2
def diferencia(c1, c2):
    """
    Ejemplo:
        A = Conjunto(["leer", "escribir", "admin"])
        B = Conjunto(["leer"])
        diferencia(A, B) -> {"escribir", "admin"}
    """
    # TODO
    pass

### SOLUCIÓN ###

def interseccion(c1, c2):
    resultado = Conjunto()
    actual = c1.cabeza
    while actual:
        if c2.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado

def union(c1, c2):
    resultado = Conjunto()
    actual = c1.cabeza
    while actual:
        resultado.agregar(actual.dato)
        actual = actual.siguiente
    actual = c2.cabeza
    while actual:
        resultado.agregar(actual.dato)  # agregar() ya ignora duplicados
        actual = actual.siguiente
    return resultado

def diferencia(c1, c2):
    resultado = Conjunto()
    actual = c1.cabeza
    while actual:
        if not c2.pertenece(actual.dato):
            resultado.agregar(actual.dato)
        actual = actual.siguiente
    return resultado



# 2a (1.0 pt): Retorna True si TODAS las filas, columnas y subcuadros son válidos
def tablero_valido(tablero):
    """
    Usa validar_fila, validar_columna, validar_subcuadro.
    Retorna True solo si los 9+9+9 = 27 checks pasan.
    """
    # TODO
    pass

# 2b (1.5 pt): Retorna una lista de strings describiendo QUÉ está mal
def diagnosticar_tablero(tablero):
    """
    Ejemplo de retorno si hay errores:
        ["Fila 3 inválida", "Columna 7 inválida", "Subcuadro (3,6) inválido"]
    Si todo está bien retorna lista vacía [].
    """
    # TODO
    pass

TABLERO_INVALIDO = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]  # fila 9: 1 repetido, falta el 7
]

### SOLUCIÓN ###
def tablero_valido(tablero):
    for i in range(9):
        if not validar_fila(tablero, i): return False
        if not validar_columna(tablero, i): return False
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            if not validar_subcuadro(tablero, fi, ci): return False
    return True

def diagnosticar_tablero(tablero):
    errores = []
    for i in range(9):
        if not validar_fila(tablero, i):
            errores.append(f"Fila {i+1} inválida")
        if not validar_columna(tablero, i):
            errores.append(f"Columna {i+1} inválida")
    for fi in [0, 3, 6]:
        for ci in [0, 3, 6]:
            if not validar_subcuadro(tablero, fi, ci):
                errores.append(f"Subcuadro ({fi+1},{ci+1}) inválido")
    return errores




"""
Un usuario puede tener MÚLTIPLES roles. Sus permisos efectivos
son la UNIÓN de todos sus roles.

Roles disponibles:
    viewer  = {leer}
    editor  = {leer, escribir}
    admin   = {leer, escribir, eliminar, crear_usuarios}
"""
# 3a (1.0 pt): Dado una lista de roles, retorna el Conjunto de permisos efectivos
def permisos_efectivos(lista_roles):
    """
    lista_roles: lista de objetos Conjunto

    Ejemplo:
        permisos_efectivos([viewer, editor])
        -> Conjunto con {"leer", "escribir"}

        permisos_efectivos([viewer])
        -> Conjunto con {"leer"}
    """
    # TODO: usa la función union() del ejercicio anterior
    pass

# 3b (1.0 pt): Dado un usuario con múltiples roles, ¿puede hacer la acción?
def usuario_puede(roles_usuario, permisos_accion):
    """
    Ejemplo:
        usuario_puede([viewer, editor], accion_editar)  -> True
        usuario_puede([viewer], accion_editar)           -> False
        usuario_puede([editor, admin], accion_admin)     -> True
    """
    # TODO: usa permisos_efectivos() y tiene_permisos()
    pass

### SOLUCIÓN ###
def permisos_efectivos(lista_roles):
    resultado = Conjunto()
    for rol in lista_roles:
        resultado = union(resultado, rol)
    return resultado

def usuario_puede(roles_usuario, permisos_accion):
    efectivos = permisos_efectivos(roles_usuario)
    return tiene_permisos(efectivos, permisos_accion)

# Pruebas
viewer = Conjunto(["leer"])
editor = Conjunto(["leer", "escribir"])
admin  = Conjunto(["leer", "escribir", "eliminar", "crear_usuarios"])

accion_editar = Conjunto(["leer", "escribir"])
accion_admin  = Conjunto(["eliminar", "crear_usuarios"])

print(usuario_puede([viewer, editor], accion_editar))  # True
print(usuario_puede([viewer], accion_editar))           # False
print(usuario_puede([editor, admin], accion_admin))     # True
print(usuario_puede([editor], accion_admin))            # False


# =========================================================
# PRACTICA PARCIAL RESUELTA
# =========================================================

NUMEROS_VALIDOS = {1,2,3,4,5,6,7,8,9}


# =========================================================
# BLOQUE 1: SUDOKU
# =========================================================

def error_en_fila(tablero, num_fila):
    vistos = set()
    for num in tablero[num_fila]:
        if num in vistos:
            return num
        vistos.add(num)
    return None


def columna_valida_incompleta(tablero, num_columna):
    vistos = set()
    for fila in tablero:
        num = fila[num_columna]
        if num == 0:
            continue
        if num in vistos:
            return False
        vistos.add(num)
    return True


def faltantes_subcuadro(tablero, fila_inicio, col_inicio):
    elementos = set()
    for i in range(fila_inicio, fila_inicio + 3):
        for j in range(col_inicio, col_inicio + 3):
            elementos.add(tablero[i][j])
    return NUMEROS_VALIDOS - elementos


def validar_sudoku(tablero):
    # filas
    for i in range(9):
        if set(tablero[i]) != NUMEROS_VALIDOS:
            return False

    # columnas
    for j in range(9):
        col = [tablero[i][j] for i in range(9)]
        if set(col) != NUMEROS_VALIDOS:
            return False

    # subcuadros
    for fi in [0,3,6]:
        for ci in [0,3,6]:
            elementos = []
            for i in range(fi, fi+3):
                for j in range(ci, ci+3):
                    elementos.append(tablero[i][j])
            if set(elementos) != NUMEROS_VALIDOS:
                return False

    return True


def validar_sudoku_detallado(tablero):
    for i in range(9):
        if set(tablero[i]) != NUMEROS_VALIDOS:
            return ("fila", i)

    for j in range(9):
        col = [tablero[i][j] for i in range(9)]
        if set(col) != NUMEROS_VALIDOS:
            return ("columna", j)

    for fi in [0,3,6]:
        for ci in [0,3,6]:
            elementos = []
            for i in range(fi, fi+3):
                for j in range(ci, ci+3):
                    elementos.append(tablero[i][j])
            if set(elementos) != NUMEROS_VALIDOS:
                return ("subcuadro", (fi,ci))

    return ("ok", None)


def validar_tablero_incompleto(tablero):
    # filas
    for fila in tablero:
        nums = [x for x in fila if x != 0]
        if len(nums) != len(set(nums)):
            return False

    # columnas
    for j in range(9):
        col = [tablero[i][j] for i in range(9) if tablero[i][j] != 0]
        if len(col) != len(set(col)):
            return False

    return True


# =========================================================
# BLOQUE 2: LISTAS ENLAZADAS
# =========================================================

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Conjunto:
    def __init__(self, elementos=None):
        self.cabeza = None
        if elementos:
            for e in elementos:
                self.agregar(e)

    def pertenece(self, x):
        actual = self.cabeza
        while actual:
            if actual.dato == x:
                return True
            actual = actual.siguiente
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo


def a_lista(conjunto):
    lista = []
    actual = conjunto.cabeza
    while actual:
        lista.append(actual.dato)
        actual = actual.siguiente
    return lista


def contar(conjunto):
    c = 0
    actual = conjunto.cabeza
    while actual:
        c += 1
        actual = actual.siguiente
    return c


def union(c1, c2):
    nuevo = Conjunto()
    for x in a_lista(c1):
        nuevo.agregar(x)
    for x in a_lista(c2):
        nuevo.agregar(x)
    return nuevo


def interseccion(c1, c2):
    nuevo = Conjunto()
    actual = c1.cabeza
    while actual:
        if c2.pertenece(actual.dato):
            nuevo.agregar(actual.dato)
        actual = actual.siguiente
    return nuevo


def diferencia(c1, c2):
    nuevo = Conjunto()
    actual = c1.cabeza
    while actual:
        if not c2.pertenece(actual.dato):
            nuevo.agregar(actual.dato)
        actual = actual.siguiente
    return nuevo


def son_iguales(c1, c2):
    return (es_subconjunto(c1, c2) and es_subconjunto(c2, c1))


def clonar(conjunto):
    nuevo = Conjunto()
    for x in a_lista(conjunto):
        nuevo.agregar(x)
    return nuevo


def es_subconjunto(c1, c2):
    actual = c1.cabeza
    while actual:
        if not c2.pertenece(actual.dato):
            return False
        actual = actual.siguiente
    return True


# =========================================================
# BLOQUE 3: PERMISOS
# =========================================================

def permisos_faltantes(usuario, requeridos):
    faltan = Conjunto()
    actual = requeridos.cabeza
    while actual:
        if not usuario.pertenece(actual.dato):
            faltan.agregar(actual.dato)
        actual = actual.siguiente
    return faltan


def tiene_exactamente(u, r):
    return es_subconjunto(u, r) and es_subconjunto(r, u)


def es_superusuario(usuario, todos):
    return es_subconjunto(todos, usuario)


def puede_realizar(roles, accion):
    for rol in roles:
        if es_subconjunto(accion, rol):
            return True
    return False


def falta_permiso(usuario, requeridos):
    actual = requeridos.cabeza
    while actual:
        if not usuario.pertenece(actual.dato):
            return actual.dato
        actual = actual.siguiente
    return None


# =========================================================
# BLOQUE 4: EXTRA
# =========================================================

def es_vacio_real(conjunto):
    return conjunto.cabeza is None


def primer_elemento(conjunto):
    if conjunto.cabeza:
        return conjunto.cabeza.dato
    return None


# =========================================================
# BLOQUE 5: AJEDREZ (🔥 PROBABLE QUIZ)
# =========================================================

def torre_valida(pos1, pos2):
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def alfil_valido(pos1, pos2):
    return abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def reina_valida(pos1, pos2):
    return torre_valida(pos1, pos2) or alfil_valido(pos1, pos2)


def caballo_valido(pos1, pos2):
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return (dx, dy) in [(1,2), (2,1)]


def rey_valido(pos1, pos2):
    return max(abs(pos1[0]-pos2[0]), abs(pos1[1]-pos2[1])) == 1


# =========================================================
# BLOQUE 6: EXTRAS TIPO PARCIAL
# =========================================================

def tiene_repetidos(lista):
    return len(lista) != len(set(lista))


def faltantes_fila(tablero, num_fila):
    return NUMEROS_VALIDOS - set(tablero[num_fila])


def es_subconjunto_lista(l1, l2):
    for x in l1:
        if x not in l2:
            return False
    return True


def contar_coincidencias(c1, c2):
    count = 0
    actual = c1.cabeza
    while actual:
        if c2.pertenece(actual.dato):
            count += 1
        actual = actual.siguiente
    return count


def agregar_todos(conjunto, lista):
    for x in lista:
        conjunto.agregar(x)


def todos_tienen_permiso(usuarios, permiso):
    for u in usuarios:
        if not u.pertenece(permiso):
            return False
    return True








# =========================================================
# EXTRA 1: VALIDAR DIAGONAL SUDOKU (tipo sudoku variante)
# =========================================================

def validar_diagonales(tablero):
    """
    True si ambas diagonales tienen 1-9 sin repetir
    """
    diag1 = set()
    diag2 = set()
    
    for i in range(9):
        diag1.add(tablero[i][i])
        diag2.add(tablero[i][8 - i])
    
    return diag1 == {1,2,3,4,5,6,7,8,9} and diag2 == {1,2,3,4,5,6,7,8,9}


# =========================================================
# EXTRA 2: MATRIZ SIN REPETIDOS POR FILA Y COLUMNA
# =========================================================

def matriz_valida(matriz):
    """
    True si ninguna fila ni columna tiene repetidos
    """
    n = len(matriz)
    
    # filas
    for fila in matriz:
        if len(fila) != len(set(fila)):
            return False
    
    # columnas
    for j in range(n):
        col = [matriz[i][j] for i in range(n)]
        if len(col) != len(set(col)):
            return False
    
    return True


# =========================================================
# EXTRA 3: ELEMENTO MÁS FRECUENTE EN LISTA
# =========================================================

def mas_frecuente(lista):
    """
    Retorna el elemento que más se repite
    """
    conteo = {}
    
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
    
    max_elem = None
    max_count = 0
    
    for k, v in conteo.items():
        if v > max_count:
            max_count = v
            max_elem = k
    
    return max_elem


# =========================================================
# EXTRA 4: FILTRAR PERMISOS VÁLIDOS
# =========================================================

def permisos_validos(usuario, lista_permisos):
    """
    Retorna lista de permisos que el usuario sí tiene
    """
    resultado = []
    
    for p in lista_permisos:
        if usuario.pertenece(p):
            resultado.append(p)
    
    return resultado


# =========================================================
# EXTRA 5: AJEDREZ - CAMINO LIBRE TORRE
# =========================================================

def camino_torre_libre(tablero, pos1, pos2):
    """
    tablero: matriz con 0 vacío y 1 ocupado
    True si no hay piezas en el camino
    """
    if pos1[0] == pos2[0]:  # misma fila
        fila = pos1[0]
        c1, c2 = sorted([pos1[1], pos2[1]])
        
        for j in range(c1 + 1, c2):
            if tablero[fila][j] != 0:
                return False
    
    elif pos1[1] == pos2[1]:  # misma columna
        col = pos1[1]
        f1, f2 = sorted([pos1[0], pos2[0]])
        
        for i in range(f1 + 1, f2):
            if tablero[i][col] != 0:
                return False
    
    else:
        return False
    
    return True


# =========================================================
# EXTRA 6: ELIMINAR DUPLICADOS EN CONJUNTO (lista enlazada)
# =========================================================

def eliminar_duplicados(conjunto):
    """
    Asegura que no haya repetidos (por si agregaron mal)
    """
    vistos = set()
    actual = conjunto.cabeza
    anterior = None
    
    while actual:
        if actual.dato in vistos:
            anterior.siguiente = actual.siguiente
        else:
            vistos.add(actual.dato)
            anterior = actual
        
        actual = actual.siguiente
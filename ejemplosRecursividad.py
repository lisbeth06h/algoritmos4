#Invertir un string
#hola ==> aloh

def invertir(s):
    if len(s) <= 1:
        return s
    return invertir(s[1:]) + s[0]

# Ejemplo de uso
cadena = "hola"
cadena_invertida = invertir(cadena)
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {cadena_invertida}")






#Saber si una palabra es palindroma o no
def palindromo(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return palindromo(s[1:-1])
    

# Ejemplo de uso
palabra = "reconocer"
resultado = palindromo(palabra)
print(f"Palabra: {palabra}")
print(f"Es palindroma: {resultado}")

palabra = "hola mundo"
resultado = palindromo(palabra)
print(f"Palabra: {palabra}")
print(f"Es palindroma: {resultado}")







#contar cuantas veces se repite un caracter en un texto
def repeticiones(s, c):
    if len(s) == 0:
        return 0
    cuenta = 1 if s[0] == c else 0    
    return cuenta + repeticiones(s[1:],c)
print(repeticiones("Holaaaaaaaa", "a"))







class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
    
class Lista:
    def __init__(self):
        self.cabeza = None

    def agredar(dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = Nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

#contar cuantas veces se repite un caracter de un texto
def contar(s, c ):
    if len(s) == 0:
        return 0
    cuenta = 1 if s[0] == c else 0
    return cuenta + contar(s[1:], c)

print(contar("holaaaaaaa","a"))

#contar cuantos nodos hay en una lista
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def __len__(self):
        return self.contar(self.cabeza)

    def contar(self, nodo):
        if nodo is None:
            return 0
        return 1 + self.contar(nodo.siguiente)
    
    def contar_nodos(self):
        return self._contar_nodos_recursivos(self.cabeza)
    
    def encontrarDato(self, nodo, dato):
        if nodo is None:
            return False
        elif nodo.dato == dato:
            return True
        return self.encontrarDato(nodo.siguiente, dato)

 
lista = Lista()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

print("Cantidad de nodos:", len(lista))

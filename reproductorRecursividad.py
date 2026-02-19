class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None
    
    def duracion_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"


class Reproductor:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None
        
    def esta_vacia(self):
        return self.cabeza is None

    def insertar_final(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
            self.actual = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
            
        print("Canción agregada")

    # =========================
    # MOSTRAR LISTA (RECURSIVO)
    # =========================
    def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacía")
            return

        print("\nLista de canciones:")
        self._mostrar_recursivo(self.cabeza)

    def _mostrar_recursivo(self, nodo):
        if nodo is None:
            return
        
        if nodo == self.actual:
            print(f"{nodo.nombre} ({nodo.duracion_formato()}) <-- Reproduciendo")
        else:
            print(f"{nodo.nombre} ({nodo.duracion_formato()})")
        
        self._mostrar_recursivo(nodo.siguiente)

    # =========================
    # REPRODUCIR
    # =========================
    def reproducir(self):
        if self.actual:
            print(f"Reproduciendo: {self.actual.nombre} ({self.actual.duracion_formato()})")
        else:
            print("No hay canciones")

    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print("No hay siguiente canción")

    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print("No hay canción anterior")

    # =========================
    # ELIMINAR (RECURSIVO)
    # =========================
    def eliminar_cancion(self, nombre):
        if self.esta_vacia():
            print("Lista vacía")
            return
        
        self.cabeza = self._eliminar_recursivo(self.cabeza, nombre)

    def _eliminar_recursivo(self, nodo, nombre):
        if nodo is None:
            print("Canción no encontrada")
            return None

        if nodo.nombre == nombre:
            # Ajustar punteros
            if nodo.siguiente:
                nodo.siguiente.anterior = nodo.anterior

            if nodo.anterior:
                nodo.anterior.siguiente = nodo.siguiente
            else:
                # Si es la cabeza
                if nodo.siguiente:
                    nodo.siguiente.anterior = None

            if nodo == self.actual:
                self.actual = nodo.siguiente

            print("Canción eliminada")
            return nodo.siguiente

        nodo.siguiente = self._eliminar_recursivo(nodo.siguiente, nombre)
        return nodo


# =========================
# MENÚ
# =========================
def menu():
    print("\nREPRODUCTOR DE CANCIONES")
    print("1. Agregar canción")
    print("2. Mostrar lista")
    print("3. Reproducir canción actual")
    print("4. Siguiente canción")
    print("5. Canción anterior")
    print("6. Eliminar canción")
    print("7. Salir")


# =========================
# PROGRAMA PRINCIPAL
# =========================
reproductor = Reproductor()

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        duracion = int(input("Duración en segundos: "))
        reproductor.insertar_final(nombre, duracion)

    elif opcion == "2":
        reproductor.mostrar_lista()

    elif opcion == "3":
        reproductor.reproducir()

    elif opcion == "4":
        reproductor.siguiente()

    elif opcion == "5":
        reproductor.anterior()

    elif opcion == "6":
        nombre = input("Nombre de la canción a eliminar: ")
        reproductor.eliminar_cancion(nombre)

    elif opcion == "7":
        print("Saliendo del reproductor...")
        break

    else:
        print("Opción inválida")

def cuenta_regresiva(n):
    if n < 0: #condición de parada
        print("Cuenta regresiva terminada")
        return
    print(n)
    cuenta_regresiva(n - 1)#llamada recursiva con n-1 para acercarnos a la condicion base

#ejemplo de uso
cuenta_regresiva(10)
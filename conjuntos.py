"""
                           CONJUNTOS
grupo de elementos -> sin orden, no hay duplicados, deben ser distinguibles
conjunto: A = {1, 2, 3, 4, 5}
cardinalidad: |A| = 5
conjunto vacío: conjunto sin elementos -> A = {}
conjunto unitario: conjunto con un solo elemento -> A = {1}
un conjunto pertenece ∈ o no pertenece  ∉: A = {1, 2, 3} -> 1 ∈ A, 4 ∉ A
En python: in, not in
Union: A ∪ B = {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5} En python: A|B o A.union(B)
Intersección: A ∩ B = {1, 2, 3} ∩ {3, 4, 5} = {3} En python: A&B o A.intersection(B)
Diferencia: A - B = {1, 2, 3} - {3, 4, 5} = {1, 2} ---A-B != B-A---  En python: A-B o A.difference(B) 
Diferencia simétrica: A Δ B = (A - B) ∪ (B - A) = {1, 2, 4, 5} En python: A^B o A.symmetric_difference(B)


                         SUBCONJUNTOS
Subconjunto propio: A ⊂ B -> A = {1, 2} ⊂ B = {1, 2, 3}
igualdad de conjuntos: A = B -> A = {1, 2, 3} = B = {1, 2, 3}
conjuntos disjuntos: A ∩ B = {} -> A = {1, 2} y B = {3, 4} son disjuntos porque no tienen elementos en común

"""

lista = [5, 5, 5, 5, 2, 4, 5, 3, 6, 7, 2, 1, 5, 3, 9, 0, 1, 0, 2, 5, 7, 6]
conjunto = set(lista) #Elimina los elementos duplicados y no tiene un orden específico
conjunto = list(set(lista)) #Convertir la lista en conjunto y el conjunto en lista
print(conjunto) #Imprime el conjunto resultante, que contiene los elementos únicos de la lista
print(len(conjunto)) #Imprime la cantidad de elementos únicos en el conjunto





canciones_Juan ={
    "La Camisa Negra", "A Dios le Pido", "Me Enamora",
    "Volverte a Ver", "Es Por Ti", "La Flaca", "Oye Como Va", 
    "Es Por Ti", "La Flaca", "Oye Como Va"
}
canciones_Maria = {
    "Shape of you", "Despacito", "Me Enamora", 
    "Volverte a Ver", "Es Por Ti", "La Flaca", 
    "Oye Como Va", "Rolling in the Deep", "Someone Like You"
}
playlist_comun = canciones_Juan.intersection(canciones_Maria) #Intersección de los conjuntos
catalogo = canciones_Juan | canciones_Maria #Unión de los conjuntos
recomendaciones = canciones_Juan - canciones_Maria #Diferencia de los conjuntos
a = {canciones_Juan, canciones_Maria} #Conjunto de conjuntos
exclusivas = canciones_Juan ^ canciones_Maria #Diferencia simétrica de los conjuntos






algoritmos = {
    "Ana", "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan"
}

bases_de_datos = {
    "Carlos", "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge"
}
redes = {
    "Diana", "Eduardo", "Fernanda",
    "Gabriel","Helena", "Ivan", "Jorge", "Karla"
}
estudian_todas = algoritmos & bases_de_datos & redes #Intersección de los conjuntos
estudian_algoritmos = algoritmos - (bases_de_datos | redes) #Diferencia de algoritmos con la unión de bases de datos y redes
estudian_algoritmos_redes = (algoritmos & redes) - bases_de_datos #Intersección de algoritmos y redes menos la intersección de algoritmos y bases de datos
estudian_algoritmos_o_redes = algoritmos | redes #Unión de algoritmos y redes
estudian_algoritmos_no_redes = algoritmos - redes #Diferencia de algoritmos con redes
solo_algoritmos = algoritmos - bases_de_datos - redes #Diferencia de algoritmos con la unión de bases de datos y redes
solo_bases_de_datos = bases_de_datos - algoritmos - redes #Diferencia de bases de datos con la unión de algoritmos y redes
solo_redes = redes - algoritmos - bases_de_datos #Diferencia de redes con la unión de algoritmos y bases de datos
solo_una_materia = solo_algoritmos | solo_bases_de_datos | solo_redes #Unión de los tres conjuntos menos la intersección de los tres conjuntos
print(len(solo_una_materia))

reporte = {}
todos = algoritmos | bases_de_datos | redes
for estudiante in todos:
    materias = []
    if estudiante in algoritmos:
        materias.append("Algoritmos")
    if estudiante in bases_de_datos:
        materias.append("Bases de Datos")
    if estudiante in redes:
        materias.append("Redes")
    reporte[estudiante] = materias
print(reporte)





catalogo = {
    "Inception": {"ciencia ficción", "acción", "thriller", "drama"},
    "The Matrix": {"ciencia ficción", "acción", "thriller"},
    "Titanic": {"drama", "romance", "histórica"},
    "The Notebook": {"romance", "drama"},
    "Avengers": {"acción", "ciencia ficción", "aventura"},
    "John Wick": {"acción", "thriller", "crimen"},
    "Interstellar": {"ciencia ficción", "drama", "aventura"},
    "The Godfather": {"crimen", "drama", "thriller"},
    "Toy Story": {"animación", "comedia", "aventura"},
    "Shrek": {"animación", "comedia", "aventura"},
}
peliculas = set(catalogo.keys())
peliculas_comunes = []
for i in range(len(peliculas)):
    for j in range(i + 1, len(peliculas)):
        p1, p2 = peliculas[i], peliculas[j]
        generos_comunes = catalogo[p1] & catalogo[p2] #Intersección de los géneros de las dos películas
        if len(generos_comunes) >= 2: #Si tienen al menos 2 géneros en común
            peliculas_comunes.append((p1, p2, generos_comunes)) #Añadir la tupla (película 1, película 2, géneros comunes) a la lista de películas comunes
print(peliculas_comunes)


favoritos_mios = {"acción","thriller","aventura"}
recomendaciones = []
for pelicula, generos in catalogo.items():
    coincidencias = favoritos_mios & generos #Intersección de los géneros favoritos con los géneros de la película
    if coincidencias:
        porcentaje = round(len(coincidencias) / len(favoritos_mios) * 100, 2)#Calcular el porcentaje de coincidencias
        recomendaciones.append((pelicula, porcentaje)) #Añadir la tupla (película, porcentaje) a la lista de recomendaciones
recomendaciones.sort(key=lambda x: x[1], reverse=True) #Ordenar las recomendaciones por porcentaje de coincidencias de mayor a menor
print(recomendaciones)
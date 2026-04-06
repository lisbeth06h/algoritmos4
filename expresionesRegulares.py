import re

texto = "Python es genial"

resultado = re.search(r"genial", texto, re.IGNORECASE) #El re.IGNORECASE hace que la búsqueda no distinga entre mayúsculas y minúsculas, por lo que encontrará "genial" sin importar si está en mayúscula o minúscula.
resultado = re.findall(r"Python", texto) #El re.findall devuelve una lista con todas las coincidencias encontradas, en este caso devolverá ["Python"] porque encuentra "Python" (con mayúscula) en el texto.    
resultado = re.match(r"Python", texto) #El re.match busca una coincidencia al inicio de la cadena, por lo que devolverá un objeto Match si encuentra "Python" al inicio del texto, o None si no lo encuentra. En este caso devolverá un objeto Match porque "Python" está al inicio del texto.

print(resultado)  # Esto devolverá el objeto Match porque encuentra "Python" (con mayúscula)
print(resultado.group())  # Esto imprimirá "Python"



texto = "Tengo 12 manzanas, 5 peras y 10 mangos."
resultado = re.findall(r"\d+", texto) #Mustrar solo los numeros
resultado = re.findall(r"\b\w+\b", texto) #Mostrar solo las palabras
print(resultado)  


texto = "gato geto gito goto guto gaato g*ato gpto"
resultado = re.findall(r"g.to", texto) #encontrar palabras que empiecen con g, terminen con to y tengan cualquier caracter entre medio
resultado = re.findall(r"^gaato", texto) #encontar la palabra gaato al inicio de la cadena
resultado = re.findall(r"gaato$", texto) #encontrar la palabra gaato al final de la cadena
resultado = re.findall(r"g[a-z]to", texto)#encontrar palabras que empiecen con g, terminen con to y tengan una letra entre medio
resultado = re.findall(r"g\d+to", texto)#encontrar palabras que empiecen con g, tengan un número y terminen con to
resultado = re.findall(r"g[^aeiou]to", texto) #encontrar palabras que empiecen con g, terminen con to y tengan una letra que no sea vocal entre medio
print(len(resultado), resultado)  # Esto imprimirá el número de coincidencias encontradas


texto = "ac abc abbc abbbc abbbbc"
resultado = re.findall(r"ab+c", texto) #Encontar 1 o mas b entre a y c
resultado = re.findall(r"ab*c", texto) #Encontar 0 o mas b entre a y c
resultado = re.findall(r"ab?c", texto) #Encontar 0 o 1 b entre a y c
print(resultado)


texto = "@gmail.com"
resultado = re.findall(r"@", texto) #Encontar el símbolo @ en el texto
print(len(resultado), resultado)



texto = "dskaohddfg@gmail.com"
resultado = re.findall(r".+@", texto) #Encontrar cualquier cosa antes de la arroba, el .+ significa que puede haber cualquier caracter (.) y que puede haber uno o mas caracteres (+) antes de la arroba (@)
resultado = re.findall(r"^.{5,10}@", texto) #Encontrar cualquier cosa antes de la arroba, el .{5,10} significa que puede haber cualquier caracter (.) y que puede haber entre 5 y 10 caracteres ({5,10}) antes de la arroba (@)

if len(resultado) > 0:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")

print(len(resultado), resultado)



texto = "Tengo un perro, un gato y un pez"
resultado = re.findall(r"perro|gato|pez", texto) #Encontrar cualquiera de las palabras "perro", "gato" o "pez" en el texto
print(resultado)


texto = "El precio es $100.000} (cien dolares)"
resultado = re.findall(r"\$\d+\.\d+", texto) #Encontrar precios en formato $100.000
resultado = re.findall(r"\(.*\)", texto) #Encontrar palabras entre paréntesis
print(resultado)


texto = "jajajajaa"
resultado = re.findall(r"(ja)+", texto) #Encontrar "ja" 
print(resultado)


texto = "JavaScript TypeScript CoffeeScript Python"
resultado = re.findall(r"\w+", texto) #Encontrar todas las palabras en el texto, el \w+ significa que puede haber cualquier caracter alfanumérico (letras, números o guiones bajos) y que puede haber uno o más caracteres (+) en cada palabra 
print(resultado)


texto = "juan@gmail.com"
resultado = re.findall(r"^\w+@\w{2,3}", texto) #Encontrar correos electrónicos que tengan un nombre de usuario alfanumérico seguido de una arroba (@) y un dominio de 2 o 3 caracteres (por ejemplo, "gmail.com" o "yahoo.co")
#w significa cualquier caracter alfanumérico (letras, números o guiones bajos)
#+ significa que puede haber uno o más caracteres alfanuméricos en el nombre de usuario
#@ es el símbolo de arroba que separa el nombre de usuario del dominio
#^ significa el inicio de la cadena
#\w{2,3} significa que el dominio debe tener entre 2 y 3 caracteres alfanuméricos (por ejemplo, "com", "net", "co", etc.)
print(resultado)





3007182344
300-7182344
def validar_celular(numero):
    telefono_valido = re.match(r"^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}", numero)#El patrón de expresión regular ^3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2} se utiliza para validar números de celular en el formato colombiano. Aquí está la explicación del patrón:
# ^: Indica el inicio de la cadena.
# 3: El número de celular debe comenzar con el dígito 3.
# \d{2}: Después del dígito 3, debe haber exactamente dos dígitos (por ejemplo, 00, 01, 02, etc.).
# [-\s]?: Permite un guion (-) o un espacio (\s) opcional después de los primeros tres dígitos.
# \d{3}: Después del guion o espacio opcional, debe haber exactamente tres dígitos (por ejemplo, 718).
# [-\s]?: Permite un guion (-) o un espacio (\s) opcional después de los tres dígitos anteriores.
# \d{2}: Después del guion o espacio opcional, debe haber exactamente dos dígitos (por ejemplo, 23).
# [-\s]?: Permite un guion (-) o un espacio (\s) opcional después de los dos dígitos anteriores.
# \d{2}: Después del guion o espacio opcional, debe haber exactamente dos dígitos (por ejemplo, 44).
    return bool(telefono_valido)

print(validar_celular("300"))
print(validar_celular("500348769"))


def validar_fecha(fecha):
    fecha_valida = re.match(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20\d{2}$)", fecha) #El patrón de expresión regular ^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20\d{2}$) se utiliza para validar fechas en formato dd/mm/yyyy o dd-mm-yyyy. Aquí está la explicación del patrón:
# ^: Indica el inicio de la cadena.
# (0[1-9]|[12]\d|3[01]): Valida el día, que puede ser un número del 01 al 09, del 10 al 29 o del 30 al 31.
# [-/]: Permite un guion (-) o una barra (/) como separador entre el día, el mes y el año.
# (0[1-9]|1[0-2]): Valida el mes, que puede ser un número del 01 al 09 o del 10 al 12.
# [-/]: Permite un guion (-) o una barra (/) como separador entre el día, el mes y el año.
# (19|20\d{2}$): Valida el año, que puede ser un número que comience con 19 o 20 seguido de dos dígitos (por ejemplo, 1990 o 2020). El $ al final indica el final de la cadena.
    return bool(fecha_valida)
print(validar_fecha("31/12/2020"))



def validar_contrasenia(contrasenia):
    if len(contrasenia) != 8:
        return False, "La contraseña debe tener exactamente 8 caracteres."
    if not re.search(r"[A-Z]", contrasenia):
        return False, "La contraseña debe contener al menos una letra mayúscula."
    if not re.search(r"[a-z]", contrasenia):
        return False, "La contraseña debe contener al menos una letra minúscula."
    if not re.search(r"\d", contrasenia):
        return False, "La contraseña debe contener al menos un número."
    if not re.search(r"[@#$%^&+=.]", contrasenia):
        return False, "La contraseña debe contener al menos un carácter especial (@#$%^&+=.)."
    return True, "La contraseña es válida."
print(validar_contrasenia("Abcdefg1"))





texto = "juan@gmail.com"

resultado = re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", texto)

if resultado:
    print("Correo válido")
else:
    print("Correo inválido")
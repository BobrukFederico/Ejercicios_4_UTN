#3

def cargar_secuencialmente(cantidad) -> list:
    lista_nombre = [0] * cantidad
    lista_sexo = [0] * cantidad
    lista_cantidad_horas = [0] * cantidad
    lista_ingreso_semanal = [0] * cantidad

    for i in range(len(lista_nombre)):
        lista_nombre[i] = input(f"Ingrese el nombre en la posicion {i}: ")
        lista_sexo[i] = input(f"Ingrese el sexo en la posicion {i}: ")
        lista_cantidad_horas[i] = input(f"Ingrese la cantidad de horas en la posicion {i}: ")
        lista_ingreso_semanal[i] = input(f"Ingrese el ingreso semanal en la posicion {i}: ")

    return lista_nombre, lista_sexo, lista_cantidad_horas, lista_ingreso_semanal


#4
def cuartil(lista_numeros):
    tam_cuartil = len(lista_numeros) // 4

    maximos = [lista_numeros[0]] * tam_cuartil
    minimos = [lista_numeros[0]] * tam_cuartil

    for i in range(tam_cuartil):

        if i > 0:
            maximos [i] = minimos[0]
            minimos [i] = maximos[0]

        for j in range(len(lista_numeros)):

            if i > 0 and (lista_numeros[j] <= minimos[i-1] or 
                        lista_numeros[j] >= maximos[i-1]):
                print(f"Iteración {i} se saltea{lista_numeros[j]}")
                continue
            elif lista_numeros[j] > maximos[i]:
                maximos[i] = lista_numeros[j]
            
            if i > 0 and (lista_numeros[j] <= minimos[i-1] or 
                        lista_numeros[j] >= maximos[i-1]):
                continue
            elif lista_numeros[j] < minimos[i]:
                minimos[i] = lista_numeros[j]

    return maximos, minimos

#5

def modificar_lista(lista):
    print("0: Nombre.\n1: Sexo.\n2: Cantidad horas.\n3: Ingreso_semanal")

    lista_indice = int(input(f"A que lista quiere acceder para modificar: "))
    if 0 <= lista_indice <= 3:
        lista_seleccionada = lista[lista_indice]
        if lista_seleccionada == 0 or lista_seleccionada == 1:
            indice_seleccionada = int(input(f"Que posicion de la lista quiere modificar: {lista_seleccionada}: "))
            print(f"Elegiste el elemento {lista_seleccionada[indice_seleccionada]}")
            lista_seleccionada[indice_seleccionada] = input("Ingrese el valor a modificar: ")   
        else:
            indice_seleccionada = int(input(f"Que posicion de la lista quiere modificar: {lista_seleccionada}: "))
            print(f"Elegiste el elemento {lista_seleccionada[indice_seleccionada]}")
            lista_seleccionada[indice_seleccionada] = int(input("Ingrese el valor a modificar: "))
    else:
        print("Error. Ese indice no esta")
    return lista


#6
def pedir_10_numeros(min, max, cantidad):
    
    numeros = [0] * cantidad

    contador = 0
    for i in range(len(numeros)):
        numeros[i] = int(input(f"Ingrese un numero para la posicion {i}: "))
        while numeros[i] < min or numeros[i] > max:
            numeros[i] = int(input(f"Fuera de rango. Ingrese un numero para la posicion {i} (Tiene que estar entre {min} y {max}): "))
    return numeros


#7

def buscar_personas_menores(lista):
    primero = True
    minimo = 0

    for i in range(len(lista)):
        if lista[i] <= minimo or primero:
            primero = False
            minimo = lista[i]
            indice = i    

    return indice


#8

def verificar_tipo_lista(lista):
    primer_tipo = type(lista[0])
    tipos_iguales = True
    tipos = []

    for i in range(len(lista)):
        tipos.append(type(lista[i]))
        if type(lista[i]) != primer_tipo:
            tipos_iguales = False
    
    if not tipos_iguales:
        return tipos
    else:
        return type(lista[0])

def cargar_datos(lista):
    for i in range(len(lista)):
        dato = input(f"Ingrese el valor en la posicion {i}:")
        if type(dato) == type(lista[i]):
            lista[i] = dato

    return lista
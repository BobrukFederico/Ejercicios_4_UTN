

def buscar_mas_joven_y_grande(lista_n, lista_e):
    hay_joven = False
    hay_grande = False
    minimo = 0
    indice_joven = 0
    maximo = 0
    indice_mayor = 0

    for i in range(len(lista_n)):
        if minimo <= lista_e[i] or not hay_joven:
            hay_joven = True
            minimo = lista_e[i]
            indice_joven = i
        
        if maximo >= lista_e[i] or not hay_grande:
            hay_grande = True
            maximo = lista_e[i]
            indice_mayor = i
    
    nombre_menor = lista_n[indice_joven]
    nombre_mayor = lista_n[indice_mayor]
    return nombre_menor, nombre_mayor


#b

def parar_mas_de_65(lista):
    for i in range(len(lista)):
        if lista[i] >= 65:
            print("Hay mayores de 65, por lo tanto se corta el bucle")
            break

    return lista


def calcular_media_etaria(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]

    promedio_edad_etaria = suma / len(lista)

    return promedio_edad_etaria
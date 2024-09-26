
#a

def calcular_ingresos_hora_20(ingresos):
    matriz_auxiliar = list(ingresos)
    n = len(matriz_auxiliar)
    contador_20 = int(n * 0.2)

    suma_top_20 = 0
    contador_top_20 = 0

    mayor_ingreso = matriz_auxiliar[0]
    indice_mayor = 0

    while contador_top_20 < contador_20:
        for i in range(1,len(matriz_auxiliar)):
            if matriz_auxiliar[i] >= matriz_auxiliar[indice_mayor]:
                mayor_ingreso = matriz_auxiliar[i]
                indice_mayor = i
    
        suma_top_20 += mayor_ingreso
        contador_top_20 += 1
        matriz_auxiliar.pop(indice_mayor)

    promedio_top = int(suma_top_20 / contador_top_20)
    return promedio_top




def calcular_ingreso_hora_todos(lista_ingresos):
    suma_respondentes = 0
    for i in range(len(lista_ingresos)):
        suma_respondentes += lista_ingresos[i]
    
    promedio_todos_respondentes = suma_respondentes / len(lista_ingresos)
    return int(promedio_todos_respondentes)




def buscar_valor_repetido(lista):
    contador = 0
    valor_repetido = 0
    max_repeticiones = 0

    for i in range(len(lista)):
        contador = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1
        if contador >= max_repeticiones:
            max_repeticiones = contador
            valor_repetido = lista[i]
    return valor_repetido


def calcular_media_geometrica(lista):
    producto = 1

    for i in range(len(lista)):
        producto *= lista[i]

    return producto ** (1 / len(lista))


def recorrer_ambos_sentidos(lista):
    print("De forma creciente")
    for i in range(len(lista)):
        print(lista[i])

    print("-------------------------")
    print("De forma descendiente")
    for j in range(len(lista) -1, -1, -1):
        print(lista[j])
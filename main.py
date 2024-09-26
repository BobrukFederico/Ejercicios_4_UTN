from funciones import *


lista_ingresos_horarios = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54,
9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]


resultado_a = calcular_ingresos_hora_20(lista_ingresos_horarios)
print(f"El porcentaje es: {resultado_a}%")


resultado_b = calcular_ingreso_hora_todos(lista_ingresos_horarios)
print(f"El porcentaje de todos los respondientes es: {resultado_b}%")


resultado_c = buscar_valor_repetido(lista_ingresos_horarios)
print(f"El valor mas repetido es: {resultado_c}")

resultado_d = calcular_media_geometrica(lista_ingresos_horarios)
print(f"La media geometrica de la lista es: {resultado_d}")

recorrer_ambos_sentidos(lista_ingresos_horarios)

#2
lista_ed = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nom = ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena","Mariela", "Ignacio"]

resultado_2_a = buscar_mas_joven_y_grande(lista_nom, lista_ed)
print(resultado_2_a)

#2-b
parar_mas_de_65(lista_ed)

#2-c
resultado_2_c = calcular_media_etaria(lista_ed)
print(f"La media etaria es: {resultado_2_c}")


#3
# resultado_3 = cargar_secuencialmente(3)
# print(resultado_3)

#4
lista_numeros = [95, 3, 55, 4, 6, 9, 13, 12, 10, 99, 33, 22, 53, 44, 67, 69, 34, 19, 86, 100]

resultado_4 = cuartil(lista_numeros)
print(resultado_4)

# #5
# resultado_5 = modificar_lista(resultado_3)

#print(resultado_5)

#6
#resultado_6 = pedir_10_numeros(0,20, 10)
#print(resultado_6)


#7
Nombres= ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

# resultado_7 = buscar_personas_menores(edades)
# print(f"El nombre de la persona mas joven es: {Nombres[resultado_7]} y su edad es: {edades[resultado_7]}")


#8
resultado_8 = verificar_tipo_lista([1,24,6,78])
print(resultado_8)
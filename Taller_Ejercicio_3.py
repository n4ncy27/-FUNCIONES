# 3. construir una función que reciba como parametro una lista de datos numericos y retome la suma de dichos numeros

def sumar_datos(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma


# lista
lista1 = [2,3,4,5,6]
suma = suma_datos(lista1)
print(suma)


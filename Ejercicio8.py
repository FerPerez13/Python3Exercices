'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.'''

def createList():
    print("Creando una lista:")
    lista = []
    kw = input()
    while kw != 'q':
        lista += kw
        kw = input()
    print(lista)
    return lista

def superposicion(a, b):
    contador = 0
    for i in a:
        for j in b:
            if i == j:
                contador = contador + 1
    return contador

print("Dame dos listas y veremos si tienen elementos en común:")
print("Dame la lista 1 (presiona q para terminar): ")
lista1 = createList()
print("Dame la lista 2 (presiona q para terminar): ")
lista2 = createList()

iguales = superposicion(lista1, lista2)

if iguales != 0:
    print(True, iguales)
else:
    print(False, iguales)
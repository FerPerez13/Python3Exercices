'''Definir una función que calcule la longitud de una lista o una cadena dada'''

def longitud(a):
    contador = 0
    for i in a:
        contador = contador + 1
    return contador

def createList():
    print("Creando una lista:")
    lista = []
    kw = input()
    while kw != 'q':
        lista += kw
        kw = input()
    print(lista)
    return lista

print("Dame una lista o una cadena y te la cuento")
print(" 1. Contar una lista")
print(" 2. Contar una cadena")
sel = input("Elige una opción: ")
if sel == '1':
    lista = createList()
    print("La longitud de la lista es: ", longitud(lista))
elif sel == '2':
    cadena = input("Introduce la cadena: ")
    print("La longitud de la cadena es: ", longitud(cadena))
else:
    print("Mala elección. Vuelve a ejecutarme")

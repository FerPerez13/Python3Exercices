'''Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.'''

def createList():
    print("Creando una lista:")
    lista = []
    kw = input()
    while kw != 'q':
        lista += kw
        kw = input()
    print(lista)
    return lista

def sum(a):
    suma = 0
    for i in a:
        suma = suma + int(i)
    return suma

def multip(a):
    mult = 1
    for i in a:
        mult = mult * int(i)
    return mult

print("*** Vamos a sumar todos los elementos de la lista ***")
lista = createList()
suma = sum(lista)
mult = multip(lista)
print("La suma total de los números es: ",suma)
print("La multiplicación total de la lista es: ", mult)

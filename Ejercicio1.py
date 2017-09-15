'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos'''

def max(a,b):
    if a > b:
        return a
    else:
        return b

print("Hola, dame dos números y yo te devolveré el mayor de los dos:")
a = input("Dime el primer número: ")
b = input("Dime el segundo número: ")

print("El número más grande de los dos es: ", max(a,b))
'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos'''

def maxOf3(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c

print("Dame tres números y te devolveré el más grande")
a = input("Primer número: ")
b = input("Segundo número: ")
c = input("Tercer número: ")
print("El número más grande de los tres es el: ", maxOf3(a,b,c))
'''Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".'''

def generar_n_caracteres(n,x):
    cadena = ''
    for i in range(int(n)):
        cadena = cadena + x
    return cadena

print("Dame un caracter y el número de veces que quieres que lo repita")
x = input("Dame el caracter que quieres repatir: ")
n = input("Cuantas veces quieres repatirlo: ")
print(generar_n_caracteres(n,x))
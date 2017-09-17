'''Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"'''

def inversa(a):
    invA = ''
    for i in a:
        invA = i + invA
    return invA

print("Vamos a invertir la cadena que introcimos a continuación:")
cadena = input("Dame la cadena que quieres que invierta: ")
print(inversa(cadena))
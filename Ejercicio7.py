'''Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.'''

def es_palindromo(a):
    invA = inversa(a)
    if a == invA:
        return True
    else:
        return False

'''Voy a utilizar la funcion inversa realizada en el Ejercicio6'''
def inversa(a):
    invA = ''
    for i in a:
        invA = i + invA
    return invA

print("Vamos a ver si encontramos pallindromos")
cadena = input("Dame la cadena: ")
print(es_palindromo(cadena))
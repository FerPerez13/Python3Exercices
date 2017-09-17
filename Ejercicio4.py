'''Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.'''

def esVocal(a):
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
        return True
    else:
        return False

a = input("Escribe un caracter y te digo si es vocal o no: ")
print(esVocal(a))
# a. Escribir una función de nombre palabra_no_tiene_letras(palabra,
# letras_prohibidas), la cual retorne True si es que los caracteres que componen
# una palabra no se encuentran en una lista de caracteres prohibidos.

def palabra_no_tiene_letras(palabra,letras_prohibidas):
    letra = None
    separada = list(palabra)
    for i in letras_prohibidas:
        for j in separada:
            if(i == j):
                letra = "existe"
    if(letra == "existe"):
        return print(False)
    else:
        return print(True)


palabra_no_tiene_letras("nico", ["h","u","e"])

palabra_no_tiene_letras("nico", ["h","o","e"])


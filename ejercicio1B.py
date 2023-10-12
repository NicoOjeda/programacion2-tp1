# b. Escribir una función de nombre es_abc(palabra) la cual retorne True siempre y
# cuando las letras que componen dicha palabra estén en orden alfabético, y False
# en caso contrario.

def es_abc(palabra):
    ordenada = sorted(palabra)
    listado = list(palabra)
    if(ordenada == listado):
        print(True)
    else:
        print(False)

es_abc("abcde")
es_abc("abgde")



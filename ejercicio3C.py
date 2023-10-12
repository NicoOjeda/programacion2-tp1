# c. Tal como sucede con la lógica proposicional, en Python muchas veces las
# expresiones booleanas pueden ser simplificadas manteniendo el valor de
# verdad de la expresión. Así, por ejemplo, (a and b) or (b and a) es equivalente
# a a and b. A continuación, intente simplificar las siguientes expresiones y
# escriba un procedimiento procesar_sentencias(a, b, c) que permita evaluar el
# valor de verdad de las expresiones ya simplificadas:

# i. (a or b) or (b and c)
def procesar_sentencias(a, b, c):
    print("ejercicio1")
    print("original= "+ str((a or b) or (b and c)))
    print("reducida= "+ str(a or (b and c)))

a=False
b=False
c=False
procesar_sentencias(a, b, c)
a=True
b=True
c=True
procesar_sentencias(a, b, c)
a=True
b=False
c=False
procesar_sentencias(a, b, c)
a=True
b=True
c=False
procesar_sentencias(a, b, c)
a=True
b=False
c=True
procesar_sentencias(a, b, c)
a=False
b=True
c=False
procesar_sentencias(a, b, c)
a=False
b=False
c=True
procesar_sentencias(a, b, c)
a=False
b=True
c=True
procesar_sentencias(a, b, c)

# ii. b and c or False
def procesar_sentencias2( b, c):
    print("ejercicio2")
    print("original= "+ str(b and c or False))
    print("reducida= "+ str(b and c))

b=False
c=False
procesar_sentencias2(b, c)
b=True
c=True
procesar_sentencias2(b, c)
b=True
c=False
procesar_sentencias2(b, c)
b=False
c=True
procesar_sentencias2(b, c)

# iii. a and b or c or (b and a)
def procesar_sentencias3(a, b, c):
    print("ejercicio3")
    print("original= "+ str((a and b) or c or (b and a)))
    print("reducida= "+ str((a and b or c)))

a=False
b=False
c=False
procesar_sentencias3(a, b, c)
a=True
b=True
c=True
procesar_sentencias3(a, b, c)
a=True
b=False
c=False
procesar_sentencias3(a, b, c)
a=True
b=True
c=False
procesar_sentencias3(a, b, c)
a=True
b=False
c=True
procesar_sentencias3(a, b, c)
a=False
b=True
c=False
procesar_sentencias3(a, b, c)
a=False
b=False
c=True
procesar_sentencias3(a, b, c)
a=False
b=True
c=True
procesar_sentencias3(a, b, c)

# iv. a == True or b == False
def procesar_sentencias4( a, b):
    print("ejercicio4")
    print("original= "+ str(a or b == False))
    print("reducida= "+ str(a or b == False))

a=False
b=False
procesar_sentencias4(a, b)
a=True
b=True
procesar_sentencias4(a, b)
a=True
b=False
procesar_sentencias4(a, b)
a=False
b=True
procesar_sentencias4(a, b)
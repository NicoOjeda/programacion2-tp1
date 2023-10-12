# e. Escribir un procedimiento numeros_par_impar(entrada) que, dada una lisa de
# números, eleve cada elemento impar en ella al cuadrado y los mueva a otra lista
# e imprima ambas. La lista de números la ingresa el usuario en forma de números
# separados por coma.
# Suponiendo que el usuario ingresa la siguiente lista:
# 1,2,3,4,5,6,7,8,9
# Entonces, la salida del programa debería ser:
# 2,4,6,8
# 1,9,25,49,81


numeros = input('Ingrese números enteros y la palabra "fin" para terminar: ')
lista=[]

def impresion(numeros):
    while numeros != "fin":
        lista.append(int(numeros))
        numeros = input('Ingrese números enteros y la palabra "fin" para terminar: ')
    print(f'Los numeros ingresados son : {lista}')

impresion(numeros)

def numeros_par_impar(entrada):
    pares=[]
    impares=[]
    for i in entrada:
        if(i%2 == 0):
            pares.append(i)
        else:
            impares.append(i**2)
    print(pares)
    print(impares)

numeros_par_impar(lista)
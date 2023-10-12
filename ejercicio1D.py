# d. Dadas dos listas, lista1 y lista2, escribir un método listas_diferencia(lista1, lista2)
# que tome ambas como parámetros e imprima dos listas, cada una con:
# i. Los elementos en común, en orden inverso.
# ii. Los elementos no comunes, en orden alfabético.
# El programa debería arrojar el siguiente resultado:
# listas(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])
# ['c', 'b']
# ['a', 'e', 'd']

def listas_diferencia(lista1, lista2):
    comun = []
    for i in lista1:
        for j in lista2:
            if(j == i): 
                comun.append(j)
    no_comun = lista1+lista2
    for e in no_comun:
        for d in lista2:
            if(d == e):
                no_comun.remove(d)
    no_comun = sorted(no_comun)
    comun2 = sorted(comun)
    comun2 = comun2[::-1]
    print(comun2)      
    print(no_comun)      

listas_diferencia(['b', 'a', 'c'], ['e', 'b', 'd', 'c'])



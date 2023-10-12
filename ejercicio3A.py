# a. Escribir una función suma(numero) que resuelva la siguiente suma, asumiendo
# que numero = 10:
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# En el programa que invoque dicha función:
# i. El usuario debe poder ingresar el valor del parámetro numero.
# ii. Debe validarse que el dato ingresado por el usuario corresponda a
# un dígito, y no a otro tipo de dato como un carácter.
# iii. El cálculo debe realizarse utilizando algún tipo de bucle (ej: for,
# while).

numero = input("Ingrese un numero: ")
while(not numero.isdigit()):
    print("El numero debe ser un digito numérico")
    numero = input("Ingrese un numero: ")

def suma(numero):
    total=0
    numero= int(numero)
    for i in range(0,numero+1):
        total+=i
    print(total)

suma(numero)

# BONUS: Luego, codificar una función equivalente que utilice recursividad.
numero2 = input("Ingrese un numero: ")

while(not numero2.isdigit()):
    print("El numero debe ser un digito numérico")
    numero2 = input("Ingrese un numero: ")
    
def suma_recursiva(numero2):
    numero2 = int(numero2)
    if(numero2==0):
        return 0
    else:
        return suma_recursiva(numero2-1) + numero2

# suma_recursiva(numero2)
res = suma_recursiva(numero2)
print(res)

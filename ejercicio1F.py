# f. Un portal web requiere un formulario de alta de usuario donde se ingrese,
# mínimamente, un usuario y su correspondiente contraseña. Escriba, en Python,
# una función contrasena_valida(contrasena) que devuelva True en caso de
# superar las siguientes validaciones sobre la contraseña proporcionada por el
# usuario:

# La salida esperada es la siguiente:
# abc.123 es válida: False
# Abc.123 es válida: False
# AbC.123 es válida: True
# AbC.1 23 es válida: False
# ÁbC.123 es válida: False
import re

def contrasena_valida(contrasena):
    contrasena_valida = True
    # i. Longitud entre 6 y 20 caracteres.
    if len(contrasena)<6 or len(contrasena)>20:
        contrasena_valida = False
    # ii. Debe contener al menos un número.    
    elif not re.search('[0-9]', contrasena):
        contrasena_valida = False
    # iii. Debe contener al menos dos mayúsculas.
    elif not re.search('[A-Z].[A-Z]', contrasena):
        contrasena_valida = False
    # v. No puede contener espacios.
    elif re.search('[\s]', contrasena):
        contrasena_valida = False
    # iv. Debe contener al menos un carácter especial.    
    elif not re.search('[$&+,:;=?@#|<>.^*()%!-]', contrasena):
        contrasena_valida = False
    return contrasena_valida

print(contrasena_valida('abc.123'))
print(contrasena_valida('Abc.123'))
print(contrasena_valida('AbC.123'))
print(contrasena_valida('AbC.1 23'))
print(contrasena_valida('ÁbC.123'))

# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro.
# La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación.
# Por defecto es del 1 al 10.

def tabla_multiplicar(n: int, inicio: int = 1, fin: int = 10) -> None:
    for i in range(inicio, fin + 1):
        print(n * i)


# Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.
# 1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def devolver_numero_entero():
    ingreso = input('Ingreso de un número entero: ')
    if ingreso.isdigit():
        return int(ingreso)
    else:
        return "el numero ingresado es inválido"


# 2)  Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def devolver_numero_flotante():
    ingreso = input('Ingreso de un número entero: ')
    if "." in ingreso:
        return float(ingreso)
    else:
        return "el numero ingresado es inválido"


# 3)  Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
def devolver_cadena():
    ingreso = input('Ingreso de una cadena: ')
    if ingreso.isalpha():
        return ingreso
    else:
        return "por favor ingrese una cadena válida"

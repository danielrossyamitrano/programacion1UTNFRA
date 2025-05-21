def sumar(a: int, b: int) -> int:
    return int(a + b)


def dividir(a: int, b: int) -> float:
    return a / b


# 1) Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
def devolver_numero_entero():
    ingreso = input('Ingreso de un número entero: ')
    if ingreso.isdigit():
        return int(ingreso)


# 2)  Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
def devolver_numero_flotante():
    ingreso = input('Ingreso de un número entero: ')
    if "." in ingreso:
        return float(ingreso)


# 3)  Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
def devolver_cadena():
    ingreso = input('Ingreso de una cadena: ')
    if ingreso.isalpha():
        return ingreso


# ESTO ESTA TODO MAAAAAAAAAAAAAAAAAAAAAL
# def solicitar_al_usuario(tipo_de_dato):
#     ingreso = input(f'ingrese un {tipo_de_dato}: ')
#     if tipo_de_dato == 'entero':
#         return devolver_numero(int(ingreso))
#     elif tipo_de_dato == 'cadena':
#         return devolver_cadena(ingreso)
#     else:
#         return devolver_flotante(float(ingreso))
####################################################


def es_float(numero):
    """Valida que el numero sea un flotante"""
    return type(numero) is float

def es_int(numero):
    """Valida que el numero sea un entero"""
    return type(numero) is int


# 4) Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.
def area_rect(base: float, altura: float) -> float:
    """Calcula el área del cuadrado tomando su base y altura"""
    if (es_float(base) or es_int(base)) and (es_float(altura) or es_int(altura)):
        return base * altura
    else:
        print('Los números ingresados son inválidos')


# 5) Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver
# el área.
def area_circulo(radio: float) -> float:
    """Calcula el área del circulo su radio. Incluye una aproximación de pi"""
    pi = 3.14159  # hay otra forma más precisa de usar pi dentro del módulo math
    if es_float(radio) or es_int(radio):
        return pi * (radio ** 2)
    else:
        print('El radio ingresado es  inválido')

# 6) Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si
# el número es par o impar.
def es_par(num: int) -> int:
    """Verifica que el número ingresado es par"""
    if es_int(num):
        if num % 2 == 0:
            return f'El número {num} es par'
        else:
            return f'El número {num} es impar'
    else:
        print('El número ingresado es inválido.')

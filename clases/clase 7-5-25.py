# 7) Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par,
# False en caso contrario.
def es_par_bool(num: int) -> bool:
    """Devuelve True o False dependiendo de la paridad del número"""
    if es_int(num):
        if num % 2 == 0:
            return True
        else:
            return False
    else:
        print('El número ingresado es inválido.')


# 8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver
# el número más grande.
def maxim(num1: int, num2: int, num3: int) -> int:
    """Encuentra el máximo numero dentro de tres numeros"""
    max_num = float("-inf")
    if es_int(num1) and es_int(num2) and es_int(num3):
        for num in [num1, num2, num3]:
            if num > max_num:
                max_num = num
        return max_num
    else:
        print('Los números ingresados son inválidos')


# 9) Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como
# argumentos y devolver el resultado.
def potencia(base: int, exponente: int) -> float:
    """Calcula la potencia de un numero por su exponente"""
    if es_int(base) and es_int(exponente):
        return base ** exponente
    else:
        print('Los números ingresados son inválidos')


# 10) Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
def es_primo(numero: int) -> int:
    """Devuelve True o False si el número es primo"""
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # No se me ocurre otra forma de verificar que número sea primo si no es buscándolo en una lista de primos.
    if es_int(numero):
        return numero in primos
    else:
        print('El numero ingresado es inválido.')


# TAREA ADEMAS DE LOS EJERCICIOS :
# 🔹 Enunciado 1: Validar número decimal (float)
# Objetivo: Crear una función que valide si un valor recibido como parámetro (string o número) puede interpretarse como un número decimal.
def es_float(numero) -> bool:
    """Valida que el numero sea un flotante"""
    return type(numero) is float


def es_un_float(cadena: str) -> bool:
    """Valida que el string contenga una cadena válida para un float."""

    cadena = cadena.replace(',', '.')  # convierte las comas en puntos, por si el número ingresado es "español".
    test_1 = '.' in cadena  # verifica que haya un punto (coma) en el número.
    test_2 = ''.join(cadena.split('.')).isdigit()  # verifica que todos los "otros" caracteres sean dígitos.
    test_3 = '.' != cadena[-1]  # verifica que el punto no esté al final del string, como en una oración típica.
    test_4 = cadena.count(".") == 1  # verifica que haya sólo un punto (coma) en el string.

    # Devuelve True si todas las pruebas son True. También podría hacerse con all(test_1, ...)
    return test_1 and test_2 and test_3 and test_4


def es_un_float_master(numero_o_string) -> bool:
    if type(numero_o_string) is not str:
        return es_float(numero_o_string)
    else:
        return es_un_float(numero_o_string)


# Enunciado:
# Escribí una función llamada es_float(valor) que reciba un solo parámetro. La función debe retornar True si el valor puede convertirse a float,
# ya sea que venga como string (por ejemplo, "3.14") o como número (3.14), y False en caso contrario.
# Probá tu función con distintos valores como "3.14", 3.14, "texto", "12", 12, y None.

# 🔹 Enunciado 2: Validar número entero (int)
# Objetivo: Crear una función que valide si un valor puede interpretarse como un número entero.


# Enunciado:
# Escribí una función llamada es_entero(valor) que reciba un solo parámetro. La función debe retornar True si el valor puede convertirse a int,
# ya sea que venga como string ("5") o como número (5), y False en caso contrario.
# Probá tu función con valores como "5", 5, "5.0", 5.0, "cinco" y None.

def es_int(numero):
    """Valida que el numero sea un entero"""
    return type(numero) is int


def es_entero(numero_o_string) -> bool:
    test_int = type(numero_o_string) is int
    test_0 = type(numero_o_string) is str
    test_1 = test_0 and numero_o_string.digit()
    test_2 = es_un_float(numero_o_string)
    test_3 = test_0 and not (test_1 or test_2)
    test_4 = numero_o_string is not None
    if test_1 or test_2 or test_int:
        return True
    elif test_3 or test_4:
        return False


# 🔹 Enunciado 3: Validar si un valor es alfanumérico
# Objetivo: Crear una función que verifique si un string es estrictamente alfanumérico.

# Enunciado:
# Escribí una función llamada es_alfanumerico(valor) que reciba un parámetro y devuelva True si es un string compuesto únicamente
# por letras y/o números (sin espacios, símbolos o acentos), y False en caso contrario.
# Probá la función con valores como "Hola123", "hola mundo", "123", "!!!", "" y None.

def es_alfanumerico(valor: str) -> bool:
    if type(valor) is str and valor.isalnum():
        return True
    else:
        return False

# from modulo_for import calcular_primo
#
#
# def ask():
#     """Esta función pide al usuario un número natural, y repite el mensaje en caso de input incorrecto"""
#     print("Por favor ingrese un número natural")
#     while True:
#         numero = input('> ')
#         if numero.isnumeric():
#             numero = int(numero)
#             break
#         else:
#             print('Número incorrecto, por favor ingrese un número natural')
#     return numero
#
#
# def todos_los_primos_hasta(n):
#     """Devuelve la cantidad de números primos encontrados comprendidos entre 1 y el número ingresado"""
#     primos_encontrados = 0
#     for numero in range(n + 1):
#         if calcular_primo(numero):
#             primos_encontrados += 1
#     return primos_encontrados
#
# # Crear una función que (utilizando el algoritmo del ejercicio de la guia de for),
# # muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro.
# # La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
# numero_ingresado = ask()
# cuantos = todos_los_primos_hasta(numero_ingresado)
# print(f"se encontraron {cuantos} números primos encontrados entre la unidad y el número {numero_ingresado}.")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print("El factorial de 5 es:", factorial(5))

# def cuenta_regresiva(n):
#     if n == 0:
#         print("¡Despegue!")
#     else:
#         print(n)
#         cuenta_regresiva(n - 1)
#
# cuenta_regresiva(5)

#modularizar




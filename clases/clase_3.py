# Ejercicio 1:
# Escribí un programa en Python que le pida al usuario ingresar su edad.
# Si la edad es menor a 0 o mayor a 120, mostrar un mensaje que diga: "Edad inválida".
# Si la edad es menor a 13, mostrar: "Acceso denegado. Debes tener al menos 13 años para entrar."
# Si la edad está entre 13 y 17 inclusive, mostrar: "Acceso restringido. Estás en modo adolescente."
# Si la edad es 18 o más, mostrar: "Acceso completo concedido."

print('Por favor ingrese su edad')
edad = int(input("Edad: "))
# Se podría parsar una frase "mi edad es 13" pero complejisaría un poco el código.
# El código como está no valida ese error, habría que incluir una clausula en el if al respecto.
if edad > 280:
    print('edad inválida')
if edad < 0 or edad >= 120:
    # usé or porque tiene que evaluar las dos condiciones, no va and porque si la primera es falsa, no evalua la segunda
    print(f"Edad '{str(edad)}' inválida.")
elif edad <= 13:
    # <= incluye también el 13.
    print("Acceso denegado. Debes tener al menos 13 años para entrar.")
elif 13 < edad <= 17:
    # Entre 14 y 17 devuelve acceso restringido. Podría ser "<= 14" también.
    print("Acceso restringido. Estás en modo adolescente.")
else:
    # la edad es mayor a 17, o sea, 18 o más.
    print("Acceso completo concedido.")


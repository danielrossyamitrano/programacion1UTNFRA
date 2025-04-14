from random import randint

# IF - ELSE -ELIF

# 1. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
# programa deberá determinar la posición del jugador en la cancha, considerando los
# siguientes parámetros:
# ● Menos de 160 cm: Base
# ● Entre 160 cm y 179 cm: Escolta
# ● Entre 180 cm y 199 cm: Alero
# ● 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese la altura del jugador en cm: "))
if altura < 160:
    print("Base")
elif 160 <= altura < 180:   
    print("Escolta")
elif 180 <= altura < 200:
    print("Alero") 
else:
    # altura >= 200
    print("Ala-Pívot o Pívot")


# 2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
# mensaje según el valor:
# ● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
# ● 4 y 5 ---> Aprobado, la nota es ...
# ● 1, 2 y 3 ---> Desaprobado, la nota es ...

nota_aleatoria = randint(1, 10)
nota = f", la nota es {nota_aleatoria}"
if nota_aleatoria >= 6:
    print(f"Promoción directa{nota}")
elif 4 <= nota_aleatoria < 6:
    print(f"Aprobado{nota}")
else:
    # nota_aleatoria <= 3
    print(f"Desaprobado{nota}")

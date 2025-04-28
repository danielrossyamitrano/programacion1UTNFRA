# Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
print('Mostrando 10 repeticiones de números ascendentes')
for i in range(11):
    print(i)

# Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
print('Mostrando 10 repeticiones de números descendentes')
for j in range(10, 0, -1):
    print(j)
# Mostrar la suma de los números desde el 1 hasta el 10.
print('Monstrando la suma de los números del 1 al 10')
suma = 0
for k in range(1, 11):
    suma += k

print(f'la suma es: {suma}')

# Mostrar la suma de los números pares desde el 1 hasta el 10.
print('Mostrando los números pares del 1 al 10')
suma_pares = 0
for l in range(0, 11, 2):
    suma_pares += l
print(f'la suma es: {suma_pares}')

# Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
suma_numeros = 0
for _ in range(5):
    suma_numeros += int(input('Ingrese un número entero: '))

print(f'La suma es: {suma_numeros}. El promedio es {suma_numeros // 5}')

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos. (while, acumulador y contador, promedio)

suma = 0
acciones = 0
print('Ingrese números, o "x" si no quiere continuar')
while True:
    accion = input('> ')
    if accion == 'x':
        print(f'la suma es {suma}, el promedio es {suma / acciones}')
        break
    elif accion in '0123456789':
        acciones += 1
        suma += int(accion)

# Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos. (while, acumulador += acumulador *=))
positivos = 0
negativos = 1
print('Ingrese números, o "x" si no quiere continuar')
while True:
    accion = input('> ')
    if accion == 'x':
        break
    elif '-' in accion:
        negativos *= int(accion)
    else:
        positivos += int(accion)

print(f'la suma de los numeros positivos es {positivos}')
print(f'el producto de los números negativos es {negativos}')

# Ingresar 10 números enteros. Determinar el máximo y el mínimo. (for, max , mix)
max_num = float('-Inf')
min_num = float('+Inf')
print('Ingresar 10 números enteros')
for _ in range(10):
    num = int(input('> '))
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f'El número mínimo es {min_num} y el máximo es {max_num}')
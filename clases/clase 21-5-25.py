# Una empresa se dedica al almacenamiento y posterior distribución de cereales en el interior del país.
# Para ello cuentan con 20 depósitos en CABA, que generalmente se encuentran en las inmediaciones de las
# estaciones del ferrocarril.
# Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo, cebada y centeno.
# La oficina central, recibe mensualmente una planilla de existencias donde se indican las existencias de cada
# cereal para cada depósito.
# Realizar un menú de opciones: while - match case

def elegir(grupo) -> int:
    """Esta función genera un menú de selección en el que usuario debe elegir entre cuatro opciones.
    Los nombres de las opciones son dadas por el parametro 'grupo'."""

    for i in range(len(grupo)):
        print(f'{i}: {grupo[i]}')

    opcion = ''
    while opcion == '':
        opcion = input('> ')
        test_1 = not opcion.isdigit()
        test_2 = len(opcion) > 1
        test_3 = (not test_1) and not (0 <= int(opcion) <= len(grupo))
        if test_1 or test_2 or test_3:
            print("Por favor ingrese un número entre 0 y 3")
            opcion = ''

    return int(opcion)


def ingresar_cantidad() -> int:
    """Carga la existencia del grano en el depósito"""

    cantidad = ''
    while type(cantidad) is not int:
        cantidad = input('> ')
        test_0 = cantidad.startswith('-')  # número es negativo
        test_1 = not test_0 and cantidad.isdigit()  # número positivo
        test_2 = test_1 and 500 <= abs(int(cantidad)) <= 20000  # abs() xq el usuario puede ingresar numeros negativos
        if test_2:
            cantidad = int(cantidad)
        else:
            print('Por favor ingrese un número entero cuyo valor absoluto esté comprendido entre 500 y 20000')

    return cantidad


def operacion_2(depositos, existencias) -> None:
    # 2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales.
    for i in range(len(depositos)):
        cantidad = existencias[i][0] + existencias[i][1] + existencias[i][2] + existencias[i][3]
        deposito = depositos[i]
        print(f"Total almacenado en {deposito}: {cantidad} kg.")


def operacion_3(depositos, cereales, existencias) -> None:
    # 3. Nombre del cereal que almaceno menos kilos en cada depósito.
    for i in range(len(depositos)):
        minimo = float("+inf")
        indice = -1
        deposito = ''
        for j in range(len(cereales)):
            existencia = existencias[i][j]
            if existencia < minimo:
                minimo = existencia
                indice = j
                deposito = depositos[i]
        else:
            print(f"{cereales[indice]} almancenó la menor cantidad de kilogramos en {deposito}")


def operacion_4(cereales, existencias) -> None:
    # 4. Máxima cantidad de kilos almacenados de cada cereal.
    print('Mostrando la máxima cantidad de kilos almacenados de cada cereal.')
    for i in range(len(cereales)):
        cereal = cereales[i]
        cantidad = 0
        for j in range(len(existencias)):
            cantidad += existencias[j][i]
        print(f'{cereal}: {cantidad} kg')


def operacion_5(depositos, existencias, valor_por_tipo) -> None:
    # 5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector con los valores
    # por kilo de cada tipo de cereal.

    recaudaciones = []
    for i in range(len(depositos)):
        recaudacion = 0
        for j in range(len(existencias)):
            recaudacion += existencias[j][i] * valor_por_tipo[j]
        recaudaciones.append(recaudacion)

    # bubble sort mejorado
    n = len(recaudaciones)
    for i in range(len(recaudaciones)):
        ordenado = False
        j = 0
        while j < n - 1 - i:
            if recaudaciones[j] > recaudaciones[j + 1]:
                aux = recaudaciones[j]
                aux2 = depositos[j]

                recaudaciones[j] = recaudaciones[j + 1]
                depositos[j] = depositos[j + 1]

                recaudaciones[j + 1] = aux
                depositos[j + 1] = aux2

                ordenado = True
            j += 1
        if not ordenado:
            break

    print(f"El depósito con mayor recaudación es el {depositos[-1]} con ${recaudaciones[-1]}")


def operacion_6(depositos, cereales, existencias) -> None:
    # 6. Cantidad de depósitos que hayan almacenado más de 50.000 kilos entre los 4 cereales.
    excedidos = 0
    for j in range(len(depositos)):
        subtotal = 0
        for i in range(len(cereales)):
            k = existencias[i][j]
            subtotal += k
        if subtotal > 50000:
            excedidos += 1

    if excedidos > 0:
        print(f'{excedidos} depósito(s) alamacenan más de 50.000 kilogramos.')
    else:
        print('Ningún depósito alcanza más de 50.000 kilogramos almacenados.')


def operacion_7(ceraales, existencias) -> None:
    # 7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Además mostrar el nombre del cereal
    # con el máximo porcentaje.
    subtotales = []
    total = 0
    for i in range(len(existencias)):
        almacenado = 0
        cereal = ceraales[i]
        for k in existencias[i]:
            almacenado += k
            total += k
        subtotales.append([cereal, almacenado])

    maximo = float("-inf")
    max_name = ''
    for cereal, acumulado in subtotales:
        porcentaje = round(acumulado / total, 2)
        if porcentaje >= maximo:
            maximo = porcentaje
            max_name = cereal
        print(f'{cereal}: {porcentaje}%')
    print(f'\nEl cereal con el máximo porcentaje almancenado es: {max_name}')


def operacion_8(cereales, depositos, existencias, valor_por_tipo) -> None:
    # 8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.
    subtotales = []
    for i in range(len(depositos)):
        subtotal = 0
        for j in range(len(cereales)):
            subtotal += existencias[j][i] * valor_por_tipo[j]
        subtotales.append(subtotal)

    #bubble sort mejorado
    n = len(subtotales)
    for i in range(len(subtotales)):
        ordenado = False
        j = 0
        while j < n - 1 - i:
            if subtotales[j] < subtotales[j + 1]:
                aux = subtotales[j]
                aux2 = depositos[j]

                subtotales[j] = subtotales[j + 1]
                depositos[j] = depositos[j + 1]

                subtotales[j + 1] = aux
                depositos[j + 1] = aux2

                ordenado = True
            j += 1
        if not ordenado:
            break

    print("Informe de recaudación")
    for i in range(len(depositos)):
        recaudacion = subtotales[i]
        deposito = depositos[i]
        print(f'{deposito}: ${recaudacion}')


def ingresar_cereales() -> None:
    cereales = ['maíz', 'trigo', 'cebada', 'centeno']
    depositos = ["Depósito A", "Deposito B", "Depósito C", "Deposito D"]
    # existencias = [
    #     [0] * len(depositos),  # maiz
    #     [0] * len(depositos),  # trigo
    #     [0] * len(depositos),  # cebada
    #     [0] * len(depositos)  # centeno
    # ]
    existencias = [  # hardcoded for debugging
        [5000, 4000, 2000, 1000],
        [100000, 2000000, 1500, 1300],
        [1000, 60000, 3000, 700],
        [100, 400, 2000, 4000]
    ]
    valor_por_tipo = [967.19, 902.71, 967.19, 7350.67]  # valor del maíz, trigo, cebada y centeno en pesos por kilo.

    # while True:
    #     print('Ingrese el cereal cuya cantidad desea ingresar')
    #     cereal = elegir(cereales)
    #
    #     print('Ingrese el depósito en el cual se haya ese cereal')
    #     deposito = elegir(depositos)
    #
    #     print(f'Ingrese la existencia de {cereales[cereal]} almacenado en el depósito "{depositos[deposito]}"')
    #     cantidad = ingresar_cantidad()
    #
    #     existencias[deposito][cereal] = cantidad
    #     print("Existencia ingresada con éxito")
    #     if not input('¿Desea continuar?').upper().startswith("S"):
    #         break

    while True:
        print("A continuación, elija la operación que desea realizar")
        operaciones = [
            "Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales.",
            "Mostar el nombre del cereal que almaceno menos kilos en cada depósito",
            "Mostrar la máxima cantidad de kilos almacenados de cada cereal.",
            "Mostrar el depósito con mayor recaudación",
            "Cantidad de depósitos que hayan almacenado más de 50.000 kilogramos entre los 4 cereales",
            "Mostrar el porcentaje de kilos de cada cereal sobre el total de kilos almacenados",
            "Generar un informe con la recaudación de cada depósito"
        ]
        for i in range(len(operaciones)):
            print(f'{i}: {operaciones[i]}')

        operacion = input('> ')
        test_1 = operacion.isdigit()
        test_2 = test_1 and 0 <= int(operacion) < len(operaciones)
        if not test_2:
            print('Operación inválida. Por favor inténtelo de nuevo', end='\n\n')
        else:
            match int(operacion):
                case 0:
                    operacion_2(depositos, existencias)
                case 1:
                    operacion_3(depositos, cereales, existencias)
                case 2:
                    operacion_4(cereales, existencias)
                case 3:
                    operacion_5(depositos, existencias, valor_por_tipo)
                case 4:
                    operacion_6(depositos, cereales, existencias)
                case 5:
                    operacion_7(cereales, existencias)
                case 6:
                    operacion_8(cereales, depositos, existencias, valor_por_tipo)
                case _:
                    print('Operación inválida')

        if not input('\n¿Desea continuar? [S/N]: ').upper().startswith("S"):
            break


ingresar_cereales()

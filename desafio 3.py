# Desafío: Sistema de Recomendación de Productos
# Una tienda online quiere mejorar su sistema de recomendaciones analizando el comportamiento de sus clientes.
# Para ello, dispone del historial de compras de dos usuarios distintos, almacenado en listas de productos.


# 📌 Objetivo: Escribir un programa en Python que permita analizar estos historiales de compra y responder las siguientes preguntas:
#  1️⃣ Productos en común: ¿Qué productos han comprado ambos usuarios?
#  2️⃣ Productos exclusivos: ¿Qué productos ha comprado cada usuario que el otro no ha adquirido?
#  3️⃣ Catálogo total: ¿Cuál sería el conjunto total de productos comprados entre los dos usuarios?
#  4️⃣ Recomendaciones: ¿Cómo podrías utilizar esta información para sugerir productos a cada usuario?
# 🎯 Requisitos:
#  ✔️ El programa debe recibir como entrada dos listas de productos (pueden ser ingresadas manualmente o predefinidas).
#  ✔️ Debe procesar y mostrar los resultados de forma clara.
#  ✔️ Se valorará el uso de funciones para estructurar el código de manera organizada.
# Validar!!!!!!
# 🔹 Extras opcionales:
# Permitir que los usuarios ingresen sus listas manualmente.
# Ampliar el programa para comparar más de dos usuarios.

def validacion(lista_de_compras: list) -> None:
    """Esta función valida que los items de la lista sean strings, devuelve un mensaje de error si no lo fueran

    Esta función existe para la compatibilidad en caso de las que las listas sean ingresadas manualmente.
    """
    if type(lista_de_compras) is list:
        for item in lista_de_compras:
            if type(item) is not str:
                indice = lista_de_compras.index(item)
                print(f"El item en la posición {indice} no es un string.")
    else:
        print("Ingrese una lista con los elementos comprados")


def productos_en_comun(compras_1: list, compras_2: list) -> list:
    """Devuelve la lista de productos en común, o el mensaje de que no hay productos en caso de no haber alguno."""

    en_comun = []
    for item in compras_1:
        if item in compras_2:
            en_comun.append(item)

    if not len(en_comun):
        return "No hay productos en común"
    else:
        return en_comun


def productos_exclusivos(compras_1: list, compras_2: list) -> list:
    """Devuelve la lista de productos que el otro no ha adquirido."""

    exclusivos = []
    for item in compras_1:
        if item not in compras_2:
            exclusivos.append(item)

    return exclusivos


def catalogo_total(*compras: list) -> list:
    """Devuelve catalogo total de compra entre todos los usuarios."""
    catalogo = []
    for item in compras:
        if item not in catalogo:
            catalogo.append(item)

    return catalogo


def recomendacion(compras_1: list, compras_2: list, usuario=1) -> list:
    """Devuelve una lista con los elementos que no existen en la lista de compras del usuario."""
    not_in = []
    compras, otro = _segregar_usuario(compras_1, compras_2, usuario)
    for item in otro:
        if item not in compras:
            not_in.append(item)

    return not_in


def _segregar_usuario(compras_1, compras_2, usuario):
    """Esta subfunción determina qué compras son de qué usuario."""

    compras, otro = None, None
    if usuario == 1:
        compras = compras_1
        otro = compras_2
    elif usuario == 2:
        compras = compras_2
        otro = compras_1

    return compras, otro


def print_recomendacion(compras_1: list, compras_2: list, usuario=1) -> list:
    """Esta fución pregunta al usuario si desea agregar a sus compras las realizadas por el otro usuario, y
    devuelve la lista completa de ítems en ese caso."""

    compras, otro = _segregar_usuario(compras_1, compras_2, usuario)
    rec = recomendacion(compras, otro, usuario)
    print('Su lista de compras no incluye los siguientes elementos')
    for item in rec:
        print(f'* {item}')

    print('¿quiere añadirlos a su lista de compras?')
    if input('>').upper().startswith("S"):
        for item in rec:
            if item not in compras:
                compras.append(item)

    return compras


def validar_usuario(cantidad: int, alternate: bool = False) -> int:
    """Esta función valida que el usuario ingrese un número de usuario válido."""

    usuario = ''
    if alternate is False:
        articulo = 'su'
        text = 'de usuario'
    else:
        articulo = 'el'
        text = "del usuario con quien desea comparse"

    while type(usuario) is not int:
        _text = f"\nIngrese {articulo} número de indentificación {text} "
        digitos = ",".join([str(i) for i in range(cantidad)])
        usuario = input(_text + f'[{digitos}]: ')
        if not (usuario.isdigit() and 0 <= int(usuario) < cantidad):
            print(f"Por favor ingrese un dígito ({digitos})")
        else:
            usuario = int(usuario)
    print("Identificación correcta")
    return usuario


def pretty_printing(articulo: str, operacion: str, resultado: list) -> None:
    """Mejora el output de las funciones que devuelven meramente listas."""

    if type(resultado) is list:
        txt = f'{articulo} {operacion} son {", ".join(resultado)}.'
    else:
        txt = resultado

    print(txt)


def interaccion():
    """Este es el bucle principal del programa."""

    cantidad_de_usuarios = ''
    while type(cantidad_de_usuarios) is not int:
        print("Ingrese la cantidad de usuarios que desea analizar': ", end=' ')
        cantidad_de_usuarios = input()
        if cantidad_de_usuarios.isdigit() and int(cantidad_de_usuarios) > 0:
            cantidad_de_usuarios = int(cantidad_de_usuarios)
        else:
            print('Por favor ingrese un número natural mayor a 0.')
    else:
        print('Ingreso correcto.')

    print("\nPor favor, ingrese las compras realizadas por cada usuario.")
    print("Realice un ingreso vacío para cambiar de usuario.")
    compras_usuario = []
    for usuario in range(cantidad_de_usuarios):
        compras_usuario.append([])
        print(f"\nIngrese las compras realizadas por el usuario #{usuario}")
        while True:
            compra = input('> ')
            if compra == '':
                break
            else:
                compras_usuario[usuario].append(compra)

    usuario = validar_usuario(len(compras_usuario))
    el_otro = validar_usuario(len(compras_usuario), True)

    # acá validamos que los productos ingresados sean strings, aunque siempre que usemos input van a ser strings.
    validacion(compras_usuario[usuario])
    validacion(compras_usuario[el_otro])

    opciones = [
        ["Los", "Productos en común", productos_en_comun],
        ["Los", "Productos exclusivos", productos_exclusivos],
        ["El", "Catálogo total", catalogo_total],
        ["Las", "Recomendaciones", print_recomendacion]
    ]

    print('\n¿qué operación quiere realizar?')
    for i in range(len(opciones)):
        nombre = opciones[i][1]
        print(f'{i}: {nombre}')

    while True:
        opcion = input('> ')
        if opcion.isdigit():
            a = opciones[int(opcion)][0]
            b = opciones[int(opcion)][1].lower()
            c = opciones[int(opcion)][2]
            if int(opcion) == 2:
                argumentos = compras_usuario
            else:
                argumentos = compras_usuario[usuario], compras_usuario[el_otro]
            pretty_printing(a, b, c(*argumentos))
        if input('\n¿Desea terminar?\n').startswith("S"):
            break


interaccion()

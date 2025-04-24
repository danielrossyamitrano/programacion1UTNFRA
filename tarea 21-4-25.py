# tarea: realizar un algoritmo donde se le pida al user que elija entre un producto u otro,
# pero que decida cuantas encuentas desea contestar (cada iteracion es un user)

cantidad_de_encuestas = ''
while not cantidad_de_encuestas.isdigit():
    cantidad_de_encuestas = input("Ingrese cuántas encuentas desea contestar: ")
    if not cantidad_de_encuestas.isdigit():
        print('Por favor ingrese un número.', end='\n\n')
else:
    n_encuestas = int(cantidad_de_encuestas)

producto_elegido = "X"
user_id = 0
while n_encuestas > 0:
    print('\nElija un producto entre A, B, C o D')
    producto_elegido = input('Producto: ')
    if producto_elegido not in "ABCD":
        print(f'El producto {producto_elegido} es inválido')
    else:
        print(f'Su número de indentificación de usuario es #{user_id} '
              f'y ha elegido el producto "{producto_elegido}"')
        user_id += 1
        n_encuestas -= 1
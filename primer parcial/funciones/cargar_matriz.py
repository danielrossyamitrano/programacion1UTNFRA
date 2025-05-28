def cargar_matriz_notas() -> list:
    """Carga la cantidad de alumnos y las notas de los mismos"""
    while True:
        n = input('Ingrese la cantidad de alumnos: ')
        if not n.isdigit() and not 0 < int(n):  # verifica que el ingreso sea un número natural y que sea mayor que 0.
            print("ingrese un número natural")
        else:
            break  # salimos del bucle porque no hay más alumnos para ingresar.

    matriz = [[] * int(n)]  # creamos una matriz horizontal de n columnas.

    for a in range(int(n)):  # hace que el prompt aparezca solo la cantidad de veces necesaria para los cada alumno.
        print(f"A continuación, ingrese las notas para el alumno #{a} o toque [Enter] para pasar al siguiente alumno.")
        while True:
            m = input(f'Ingrese una nota para el alumno {a}: ')
            test_1 = m.isdigit()  # verifica que el input sea un número
            test_2 = test_1 and 1 <= int(m) <= 10  # verifica que el input sea un número entre 1 y 10.
            test_3 = not test_1 and m == ''  # verifica que el input este en blanco para pasar al siguiente alumno.
            if test_3:
                break  # si el usuario puso un espacio en blanco, salta al siguiente alumno.
            elif not test_1 or not test_2:  # valida y si no fuera correcto imprime error.
                print('Igrese un número natural entre 1 y 10')
            else:
                matriz[a].append(int(m))  # agregamos la nota a la columna correspondiente al alumno.

    return matriz
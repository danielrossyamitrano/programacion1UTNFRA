from .factorizacion import factorial

def pedir_y_calcular_factorial():
    numero = input("Ingrese un número entero positivo: ")
    if numero.isnumeric():
        numero = int(numero)
        if numero >= 0:
            print("El factorial de", numero, "es:", factorial(numero))
        else:
            print("Debe ingresar un número mayor o igual a cero.")
    else:
        print("Error: debe ingresar solo números.")
def porcentaje_aprobados(matriz):
    # 2 – Función porcentaje_aprobados(): Calcula el porcentaje de
    # exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
    # individual. Usar contadores y acumuladores.
    for i in range(len(matriz)):
        notas_aprobadas = 0  # el acumulador se inicia en 0 por alumno.
        notas_alumno = matriz[i]  # cada fila de la matriz es el conjunto de notas del alumno
        for nota in notas_alumno:
            if type(nota) is not int:  # una validación adicional por las dudas.
                print(f"Nota {nota} inválida")  # no podemos hacer la suma si la nota no es un integer.
                break
            elif int(nota) >= 6:
                notas_aprobadas += 1 # sumamos 1 por cada nota aprobada.
        porcentaje = round(notas_aprobadas/len(notas_alumno) * 100, 2)
        # calculamos el porcentaje de las notas; round() es solo para prolijidad.

        text1 = f"El porcentaje de aprobación del alumno #{i} es:"
        text2 = f"{porcentaje}% sobre un total de {len(notas_alumno)} notas."
        print(text1, text2)
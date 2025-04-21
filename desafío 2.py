consumo = int(input('ingrese la cantidad de metros consumidos: '))
tipo = input('ingrese su tipo de cliente (Residencial, Comercial o Industrial: ')
bono = 0
iva = .21
match tipo:
    case "Residencial":
        if consumo < 30:
            bono = .1
        elif consumo > 80:
            bono = -.15
    case "Comercial":
        if consumo > 150:
            bono = .8
        elif consumo > 300:
            bono = 1.2
        elif bono < 50:
            bono = -.5
    case "Industrial":
        if consumo > 500:
            bono = .2
        elif consumo > 1000:
            bono = .3
        elif consumo < 200:
            bono = -.1
    case _:
        print(f'tipo de cliente {tipo} inválido')

sub = 7000 + (200 * consumo)
subtotal = f"Subtotal: ${sub}"
recargos = bono if bono < 0 else ''
subtotal_recargos = f"Subtotal con recargos y bonificaciones: ${sub + bono * 100}"
rec = recargos if recargos != '' else ""
if rec != "":
    print(subtotal, rec, subtotal_recargos, f'IVA: {iva * 100}%', end='\n', sep=', ')
else:
    print(subtotal, subtotal_recargos, f'IVA: {iva * 100}%', end='\n', sep=', ')
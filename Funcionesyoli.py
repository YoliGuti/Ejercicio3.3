def calcula_iva(precio):
    iva = precio * 0.19
    return(iva)

def calcula_dcto(precio):
    dscto = int(input("Ingrese el '%' de descuento: "))
    total = precio - (precio*0.1)
    return(total)

def calcula_ims():
    peso = float(input("Ingrese su peso actual (Ej: 53.100): "))
    altura = float(input("Ingrese su altura actual (Ej: 1.60): "))
    imc = peso/(altura*altura)
    if (imc < 18.5):
        print("Bajo peso")
    if (imc > 18.5 and imc <= 24.9):
        print("adecuado")
    if (imc > 25.0 and imc <= 29.9):
        print("Sobrepeso")
    if (imc > 30.0 and imc <= 34.9):
        print("Obesidad grado 1")
    if (imc > 35.0 and imc <= 39.9):
        print("Obesidad grado 2")
    if (imc > 40.0):
        print("Obesidad grado 3")
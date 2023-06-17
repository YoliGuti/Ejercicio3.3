import Funcionesyoli as fny

flag = True
while(flag):
    print("------------M E N Ú--------------")
    print("1) Calcular IVA")
    print("2) Calcular descuento")
    print("3) Calcular IMC")
    print("4) Salir")
    op = int(input("Ingrese una opción del menú: "))
    if op == 1:
        precio = int(input("Ingrese el precio del producto: "))
        print(f"El IVA del producto es:", fny.calcula_iva(precio))
    if op == 2:
        print(f"El precio final es: ", fny.calcula_dcto(precio))
    if op == 3:
        fny.calcula_ims()
    if op == 4:
        print("Está saliendo del programa")
        flag = False
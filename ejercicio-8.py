# Dado un triángulo representado por sus lados L1, L2, L3, determinar e imprimir
#una leyenda según sea: equilátero, isósceles o escálenos

lado1 = eval(input("ingrese la medida de un lado:"))
lado2 = eval(input("ingrese la medida de un lado:"))
lado3 = eval(input("ingrese la medida de un lado:"))

if lado1 == lado2:
    if lado3 == lado2:
        print("es equilátero")
    else:
        print("es isósceles")

if lado1 != lado2 & lado2 != lado3 & lado3 != lado1:
    print("es escáleno")



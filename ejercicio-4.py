#una tienda ofrece un descuento del 15% sobre el total de la compra y
#un cliente desea saber cuanto deberá pagar finalmente por su compra.
cont = 0
x= eval(input("ingrese importe:(finaliza con -1)"))
while x >0:
    cont = cont + x
    x = eval(input("ingrese importe(finalizar con un negativo): "))

def aplicarDescuento(numero):
    return numero*15/100

print("total a pagar es:", cont - aplicarDescuento(cont))


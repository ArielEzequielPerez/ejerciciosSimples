# A partir de un valor entero ingresado por teclado, se pide informar:
#a) La quinta parte de dicho valor
#b) El resto de la división por 5
#c) La séptima parte del resultado del punto a)

x = eval(input("ingrese un numero:"))
quintaParte = x / 5
restoDivision = x % 5
septimaParte = x / 7

print("la quinta parte de", x, "es:", quintaParte)
print("el resto de dividir por 5 es :", restoDivision)
print("la septima parte de la quinta parte es:", septimaParte)

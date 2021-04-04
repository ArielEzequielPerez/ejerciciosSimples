#Ingresar e informar valores, mientras que el valor ingresado no sea negativo.
#Informar la cantidad de valores ingresados.

contador = 1
numero = eval(input("ingrese un numero: "))

while numero > 0:
    contador = contador + 1
    numero = eval(input("ingrese un numero: "))

print("la cantidad de numeros ingresados es:", contador)


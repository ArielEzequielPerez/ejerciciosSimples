# Dados 50 números enteros, informar el promedio de los mayores que 100 y la
# suma de los menores que –10.

acumuladorA = 0
acumuladorB = 0
contador = 0

for i in range(5):
    numero = eval(input("ingrese un numero:"))
    if numero > 100:
        acumuladorA = acumuladorA + numero
        contador = contador + 1
    elif numero < -10:
        acumuladorB = acumuladorB + numero

promedio = acumuladorA / contador
print("el promedio de los mayores a 100", promedio)
print("suma total de los menores de -10 es:", acumuladorB)



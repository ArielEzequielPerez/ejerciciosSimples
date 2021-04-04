#Dados 10 valores informar el mayor
lista = []
def agregarLista(numero):
    return lista.append(numero)
for i in range(10):
    numero = eval(input("ingrese un numero:"))
    agregarLista(numero)

print("el mayor numero es:", max(lista))

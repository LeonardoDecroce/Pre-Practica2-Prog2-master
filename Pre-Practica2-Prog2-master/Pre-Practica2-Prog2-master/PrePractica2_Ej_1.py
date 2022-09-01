#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
listaNum = []
listaNum.append(input("Ingrese el primer numero:"))
listaNum.append(input("Ingrese el siguiente numero:"))

print(max(listaNum[0], listaNum[1]))
if listaNum[0] > listaNum[1]:
    print(listaNum[0])
else:
    print(listaNum[1])
#FIN
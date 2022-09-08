'''
2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
mismo tiempo en sentido inverso al ingresado
'''
contador = 1
frutas=[]

while contador <= 2:

    fruta={}

    fruta['nombre']=input("Digite el nombre de la fruta: ")
    fruta['color']=input("Digite el color de la fruta: ")
    fruta['precio']=input("Digite el precio de la fruta: ")
    frutas.append(fruta)
    contador=contador+1

frutas.reverse()
for fruta in frutas:
    print(fruta, end=", ")
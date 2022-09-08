""" 1.Construir un programa que permita ingresar N (cantidad digitada por
el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
fueron ingresados  """
contador = 1

contadorMultiplodos= 0
contadorMultiplotres= 0
contadorMultiplo= 0

while contador <=5:

    numero=int(input("Digite un numero: "))

    if numero % 2 == 0 and numero % 3 == 0:
        print(f'El numero es multiplo de 2 y 3')
        contadorMultiplo=contadorMultiplo+1
    elif numero % 3 == 0: 
        print(f'El numero es multiplo de 3')
        contadorMultiplotres=contadorMultiplotres+1
    elif numero % 2 == 0:

        print(f'El numero es multiplo de 2')
        contadorMultiplodos=contadorMultiplodos+1

    contador=contador+1

print(f'El numero de multiplos de 2 y 3 ingresados fue {contadorMultiplo}')
print(f'El numero de multiplos de 2 ingresados fue {contadorMultiplodos}')
print(f'El numero de multiplos de 3 ingresados fue {contadorMultiplotres}')
""" 3.Construir un programa para ir de compras en un supermercado
que permita la construcción del siguiente MENU:

1. Digitar 1 para recibir {código, nombre, precio} de un producto 
2. Digitar 2 para mostrar todos los productos registrados 
3. Digitar 3 para permitir buscar por código un producto y editar el precio
de este 
4. Digitar 4 para permitir buscar por código un producto y eliminar el
producto 
5. Digitar 0 para SALIR
 """

opcion=100

print("1. Digitar 1 para recibir {código, nombre, precio} de un producto")
print("Digitar 2 para mostrar todos los productos registrados")
print("3. Digitar 3 para permitir buscar por código un producto y editar el precio de este")
print("4. Digitar 4 para permitir buscar por código un producto y eliminar el producto ")
print("5. Digitar 0 para SALIR")

productos=[]
bandera = True
while(opcion !=0 ):

    producto={}

    opcion=int(input("Digite ls opción preferida: "))

    if(opcion==1):
        producto['codigo']=input("Digite el codigo del producto: ")
        producto['nombre']=input("Digite el nombre del producto: ")
        producto['precio']=input("Digite el precio del producto: ")
        productos.append(producto)
    
    elif(opcion==2):
        print(productos)
    elif(opcion==3):
        codigo = input("Digite el codigo: ")
        for producto in productos:
            if producto['codigo']==codigo:
                bandera=True
                producto['precio']=input("Digite el nuevo precio del producto: ")
            else:
                bandera=False
        if bandera:
            print(f"id del producto encontrado: {producto['codigo']}")
        else:
            print("id del producto no encontrado")
    elif(opcion==4):
        codigo = input("Digite el codigo: ")
        for producto in productos:
            if producto['codigo']==codigo:
                bandera=True
                
                productos.remove(codigo)
            else:
                bandera=False
        if bandera:
            print(f"id del producto encontrado: {producto['codigo']}")
        else:
            print("id del producto no encontrado")
    elif(opcion==0):
        break
    else:
        print("Digite una opción válida")
else:
    print("Que tenga un buen día")
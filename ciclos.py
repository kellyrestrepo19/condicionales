opcion=int(print("dijita una opcion:"))
    print("Departamento d econfeccion")
    print("1.ingresar producto a fabrica")
    print("2.mostrar inventario en fabrica")
    print("0. salir")
listadoProducto =[]
while opcion!=0:
    
    opcion=int(print("dijita una opcion:"))
    if opcion==1:
        print("Digita el producto que ingresa a fabricacion:")
        #agregar un producto a la lista de productos
        listadoProducto.append(producto)
    elif opcion==2:
        print("mostrando el inventario:")
        print(listadoProducto)
    else:
        print("oipcion")
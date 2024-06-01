def tomaInventario():
    inventario = []

    while True:
    
        nombre_producto = input("Ingresa el nombre del producto (o 'salir' para finalizar): ")

        if nombre_producto.lower() == 'salir':
            break


        cantidad = int(input(f"Ingresa la cantidad de {nombre_producto}: "))


        inventario.append((nombre_producto, cantidad))


    print("\nInventario:")
    total_productos = 0
    for producto, cantidad in inventario:
        print(f"{producto}: {cantidad}")
        total_productos += cantidad

    print(f"\nTotal de productos en el inventario: {total_productos}")


tomaInventario()

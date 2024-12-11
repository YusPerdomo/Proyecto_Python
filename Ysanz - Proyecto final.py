#------------------------------------------------
#La aplicación debe ser capaz de registrar, actualizar, eliminar y mostrar productos en el inventario. Además,
#debe incluir funcionalidades para realizar búsquedas y generar reportes de productos con bajo stock.
#------------------------------------------------


#Diccionario de productos de ropa
productos = {
    "001": { "nombre": "Camiseta Básica","cantidad": 20,"precio": 10.99,"talla": "M","color": "Blanco"},
    "002": { "nombre": "Jeans Slim Fit", "cantidad": 15, "precio": 29.99, "talla": "32", "color": "Azul" },
    "003": { "nombre": "Sudadera con Capucha", "cantidad": 10, "precio": 24.99, "talla": "L",  "color": "Negro" },
    "004": { "nombre": "Vestido Casual", "cantidad": 8, "precio": 35.50, "talla": "S", "color": "Rojo"},
    "005": { "nombre": "Chaqueta de Cuero", "cantidad": 5, "precio": 59.99, "talla": "M", "color": "Negro"} }


#------------------------------------------------
# funciones:
#------------------------------------------------
# Función para crear un producto
def crear_producto():
    if productos:
        max_codigo = max(int(codigo) for codigo in productos.keys())
        nuevo_codigo = str(max_codigo + 1).zfill(3)  # Genera el nuevo código con tres dígitos
    else:
        nuevo_codigo = "001"

    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio: "))
    talla = input("Ingrese la talla: ")
    color = input("Ingrese el color: ")

    productos[nuevo_codigo] = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "talla": talla,
        "color": color
    }
    print(f"Producto agregado con éxito con el código {nuevo_codigo}.")

# Función para Listar producto seleccionado    
def producto_selecionado():
    codigo = input("Ingrese el código del producto a listar: ")
    if codigo in productos:
        producto = productos[codigo]
        print("\n--- Detalles del Producto ---")
        print(f"Código: {codigo}")
        print(f"Nombre: {producto['nombre']}")
        print(f"Cantidad: {producto['cantidad']}")
        print(f"Precio: {producto['precio']}")
        print(f"Talla: {producto['talla']}")
        print(f"Color: {producto['color']}")
    else:
        print("El producto no existe.")

# Función para actualizar un producto
def actualizar_producto():
    if codigo in productos:
        print("Deje en blanco si no desea modificar el valor.")
        nombre = input(f"Nombre actual ({productos[codigo]['nombre']}): ") or productos[codigo]['nombre']
        cantidad = input(f"Cantidad actual ({productos[codigo]['cantidad']}): ")
        cantidad = int(cantidad) if cantidad else productos[codigo]['cantidad']
        precio = input(f"Precio actual ({productos[codigo]['precio']}): ")
        precio = float(precio) if precio else productos[codigo]['precio']
        talla = input(f"Talla actual ({productos[codigo]['talla']}): ") or productos[codigo]['talla']
        color = input(f"Color actual ({productos[codigo]['color']}): ") or productos[codigo]['color']

#Actualiza producto con los nuevos valores introducido por el usuario.

        productos[codigo] = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "talla": talla,
            "color": color
            }
        print("Producto actualizado con éxito.")
    else:
        print("El producto no existe.")
    

# Función para eliminar un producto
def eliminar_producto():
    if codigo in productos:
        del productos[codigo]
        print("Producto eliminado con éxito.")
    else:
        print("El producto no existe.")

# Función para listar todos los productos
def lista_productos():
    if productos:
        print("\n--- Lista de Productos ---")
        for codigo, datos in productos.items():
            print(f"Código: {codigo}")
            print(f"  Nombre: {datos['nombre']}")
            print(f"  Cantidad: {datos['cantidad']}")
            print(f"  Precio: {datos['precio']}")
            print(f"  Talla: {datos['talla']}")
            print(f"  Color: {datos['color']}")
            print("-" * 20)
    else:
        print("No hay productos registrados.")       

# Función para Listar producto con bajo Stock.   

def bajo_Stock():
    
    for codigo, datos in productos.items():
            if datos["cantidad"]  <= 10:
                print("\n--- Lista de Productos bajo Stock ---")
                print(f"  Nombre: {datos['nombre']}")
                print(f"  Cantidad: {datos['cantidad']}")
                print(f"  Talla: {datos['talla']}")
                print(f"  Color: {datos['color']}")
                print("-" * 20)
            else:
                print(f"  Producto con Stock.")
                print(f"  Nombre: {datos['nombre']}")
                print(f"  Cantidad: {datos['cantidad']}")
                print("-" * 20)   

#funcion de la lista de opciones/Menu
def Menu ():
    global opcion
    while True:
        mostrar_Menu = input ("Quiere que muestre el menu N/S:  \n")
        if mostrar_Menu == "n" or mostrar_Menu == "N" :
            opcion = int(input("Por favor , Ingrsa la opcion del 1 al 7 que desceas gestionar : "))
            break
        elif mostrar_Menu == "s" or mostrar_Menu == "S":        
            print(" " * 20 ," A continuacion se le presentara el Memu de Gestion de Producto:   \n ")
            print(" " * 23 ," 1. Alta de Productos Nuevos. ")
            print(" " * 23 ," 2. Consulta de datos de productos. ")
            print(" " * 23 ," 3. Modificar la cantida de Stock de los productos. ")
            print(" " * 23 ," 4. Dar de baja Productos. ")
            print(" " * 23 ," 5. Listado completo de los productos. ")
            print(" " * 23 ," 6. Lista de producto con bajo Stock. ")
            print(" " * 23 ," 7. Salir  \n ")
            opcion = int(input( "Por favor , Ingrsa la opcion del 1 al 7 que desceas gestionar : "))
            break
        else:
            print("ingreso datos no validos intenetelo de nuevo")

#------------------------------------------------
#  definicion del menu principal que se muestra por 1era vez
print("-" * 101 , "  \n" ) 
print( "*" * 35 , "Bienvenidos a la Tienda Ysanz" ,  "*" * 35 , "  \n")
print("-" * 101  , "  \n" ) 
print(" " * 20 ," A continuacion se le presentara el Memu de Gestion de Producto:   \n ")
print(" " * 23 ," 1. Alta de Productos Nuevos. ")
print(" " * 23 ," 2. Consulta de datos de productos. ")
print(" " * 23 ," 3. Modificar la cantida de Stock de los productos. ")
print(" " * 23 ," 4. Dar de baja Productos. ")
print(" " * 23 ," 5. Listado completo de los productos. ")
print(" " * 23 ," 6. Lista de producto con bajo Stock. ")
print(" " * 23 ," 7. Salir  \n ")
opcion = int(input( "Por favor , Ingrsa la opcion del 1 al 7 que desceas gestionar : "))

# Parte2:  Menu de opciones:
# gestion_producto = True
while True:
# Solicitud de la opcion que desea gestionar:
#Menu principal


# Crear producto, condiciones para controlar opciones del menú.
    if opcion >= 1 and opcion <= 7: 
            if opcion == 1:
                crear_producto()
                Menu()
 # Listar producto seleccionado
            elif opcion == 2:
                producto_selecionado()
                Menu()
#Actualizar datos de un producto, buscando por codigo de producto.
            elif opcion == 3:
                codigo = input("Ingrese el código del producto a actualizar: ")
                actualizar_producto()
                Menu()
# Eliminar producto
            elif opcion == 4:
                codigo = input("Ingrese el código del producto a eliminar: ")
                eliminar_producto()
                Menu()
# Listar productos
            elif opcion == 5:
                lista_productos()    
                Menu()
# Listar producto con bajo Stock.        
            elif opcion == 6:
               
                print("\n--- Lista de Productos en Stock ---")
                bajo_Stock()            
                Menu()
# Salir  del sistema
            elif opcion == 7:
                print("Saliendo del sistema. ¡Hasta luego!")
                break
# Opción inválida
    else:
        print("Opción no válida. Intente de nuevo.")
        Menu()
        

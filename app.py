"""
app.py
Programa principal del sistema de administración de productos.
Crea los diccionarios de datos, gestiona el menú interactivo y
la interacción con el usuario. Toda la lógica reutilizable está
en modulo.py y se le pasan los diccionarios como parámetros.
"""

import modulo

# ============================================================
# DICCIONARIOS DE DATOS (únicos, creados solo aquí)
# ============================================================

productos = {
    "P101": ["Cuaderno", "Papelería", 2490, True],
    "P102": ["Lápiz", "Papelería", 590, True],
    "P103": ["Botella", "Accesorios", 6990, False],
    "P104": ["Mochila", "Accesorios", 24990, True]
}

inventario = {
    "P101": [30, 15],
    "P102": [120, 50],
    "P103": [0, 10],
    "P104": [8, 25]
}

# ============================================================
# FUNCIONES DE LECTURA DE DATOS CON VALIDACIÓN (viven en app.py
# porque interactúan directamente con el usuario)
# ============================================================

def leer_nombre():
    while True:
        nombre = input("Nombre del producto: ")
        if modulo.validar_nombre(nombre):
            return nombre.strip()
        print("El nombre no puede estar vacío")

def leer_categoria():
    while True:
        categoria = input("Categoría del producto: ")
        if modulo.validar_categoria(categoria):
            return categoria.strip()
        print("La categoría no puede estar vacía")

def leer_precio():
    while True:
        try:
            precio = int(input("Precio del producto: "))
            if modulo.validar_precio(precio):
                return precio
            print("El precio debe ser un entero mayor que cero")
        except ValueError:
            print("Debe ingresar un número entero válido")

def leer_disponible():
    while True:
        opcion = input("¿Disponible? (s/n): ")
        if modulo.validar_disponible(opcion):
            return opcion.strip().lower() == "s"
        print("Debe ingresar 's' o 'n'")

def leer_stock():
    while True:
        try:
            stock = int(input("Stock inicial: "))
            if modulo.validar_stock(stock):
                return stock
            print("El stock debe ser un entero mayor o igual a cero")
        except ValueError:
            print("Debe ingresar un número entero válido")

def leer_vendidos():
    while True:
        try:
            vendidos = int(input("Unidades vendidas: "))
            if modulo.validar_vendidos(vendidos):
                return vendidos
            print("Los vendidos deben ser un entero mayor o igual a cero")
        except ValueError:
            print("Debe ingresar un número entero válido")

def leer_codigo_nuevo():
    while True:
        codigo = input("Código del nuevo producto: ")
        if modulo.validar_codigo(codigo, productos):
            return codigo.strip()
        print("Código inválido o ya existente")

# ============================================================
# OPCIONES DEL MENÚ
# ============================================================

def opcion_stock_categoria():
    categoria = input("Ingrese la categoría a consultar: ")
    modulo.stock_categoria(categoria, productos, inventario)

def opcion_buscar_precio():
    try:
        precio_min = int(input("Precio mínimo: "))
        precio_max = int(input("Precio máximo: "))
        if precio_min < 0 or precio_max < 0 or precio_min > precio_max:
            print("El rango de precios ingresado no es válido")
            return
        modulo.buscar_precio(precio_min, precio_max, productos, inventario)
    except ValueError:
        print("Debe ingresar valores numéricos válidos")

def opcion_actualizar_precio():
    continuar = "s"
    while continuar == "s":
        codigo = input("Ingrese el código del producto a actualizar: ")
        if modulo.buscar_codigo(codigo, productos):
            nuevo_precio = leer_precio()
            modulo.actualizar_precio(codigo, nuevo_precio, productos)
            print("Precio actualizado correctamente")
        else:
            print("Código inexistente")

        continuar = input("¿Desea actualizar otro precio? (s/n): ").strip().lower()

def opcion_agregar_producto():
    codigo = leer_codigo_nuevo()
    nombre = leer_nombre()
    categoria = leer_categoria()
    precio = leer_precio()
    disponible = leer_disponible()
    stock = leer_stock()
    vendidos = leer_vendidos()

    agregado = modulo.agregar_producto(
        codigo, nombre, categoria, precio, disponible, stock, vendidos,
        productos, inventario
    )

    if agregado:
        print("Producto agregado correctamente")
    else:
        print("No fue posible agregar el producto: el código ya existe")

def opcion_eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    eliminado = modulo.eliminar_producto(codigo, productos, inventario)
    if eliminado:
        print("Producto eliminado correctamente")
    else:
        print("Código inexistente")

def opcion_mostrar_productos():
    modulo.mostrar_productos(productos, inventario)

# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Stock por categoría")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Mostrar productos")
    print("7. Salir")
    print("===================================")

def main():
    opcion = 0
    while opcion != 7:
        mostrar_menu()
        opcion = modulo.leer_opcion()

        match opcion:
            case 1:
                opcion_stock_categoria()
            case 2:
                opcion_buscar_precio()
            case 3:
                opcion_actualizar_precio()
            case 4:
                opcion_agregar_producto()
            case 5:
                opcion_eliminar_producto()
            case 6:
                opcion_mostrar_productos()
            case 7:
                print("Saliendo del sistema...")

if __name__ == "__main__":
    main()

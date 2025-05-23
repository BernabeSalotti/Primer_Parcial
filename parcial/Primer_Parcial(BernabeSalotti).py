from funciones_parcialBernabeSalotti import *

productos = ["A", "B", "C"]

ventas = [[50, 60, 70],  # Producto A
          [80, 55, 45],  # Producto B
          [40, 65, 75]]  # Producto C

separador = "----------------------------------"
seguir = "s"
while seguir == "s":
    opcion = 0
    while opcion <1 or opcion >6:
        print('\n---------MENU DE OPCIONES---------\n ' \
        '1. Mostrar productos y ventas \n ' \
        '2. Ordenar productos de mayor a menor por ventas anuales \n ' \
        '3. Buscar productos por nombre y mostrar sus ventas \n ' \
        '4. Buscar monto de venta en matriz \n ' \
        '5. Salir')
        opcion = int(input('\n-Ingrese una de las opciones segun su numeracion (1-5): '))

    if opcion == 1:
        print(separador)
        mostrar_datos(productos,ventas)
        print(separador)

    elif opcion ==2:
        print(separador)
        ordenar_may_men_totales(productos,ventas)
        print(separador)

    elif opcion ==3:
        print(separador)
        producto = input('-ingrese el producto del que desa saber sus ventas(A,B,C): ').upper()
        while producto != "A" and producto != "B" and producto != "C":
            producto = input('-ingrese un producto valido(A,B,C):  ').upper()
        print(separador)
        buscar_producto(productos,ventas,producto)

    elif opcion ==4:
        print(separador)
        print('|  valores |')
        for i in range (len(ventas)):
            for j in range(len(ventas[i])):
                print('|   ',ventas[i][j],'   |')
        valor_buscado = int(input('ingrese que valor desea buscar: '))
        print(separador)
        buscar_valor(productos,ventas,valor_buscado)
       
    elif opcion == 5:
        seguir = "n"

print('¡¡Adios!!')


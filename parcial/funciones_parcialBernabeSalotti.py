def mostrar_datos (productos: list, ventas:list)->None:
    """
    -Funcion
    Muestra una tabla con los productos, sus ventas por trimestre
    y el total por fila.

    -Parametros
    "productos" (list):lista de productos 
    "ventas" : matriz con valores de venta por trimestre

    -Procedimiento
    recorre la matriz ventas 
    muestra por consola el producto y los tres valores de cada trimestre de ese producto 
    llama a la funcion "calcular_totales" para calcular el total de la suma de los trimestres de ese producto
    """
    print('Producto | T1 | T2 | T3 | Totales')
    print('---------------------------------')
    for i in range(len(ventas)):
            print ('   ',productos[i],'   |' ,ventas[i][0], '|' ,ventas[i][1],'|' ,ventas[i][2],'|' ,calcular_totales(ventas)[i])

def calcular_totales (ventas:list)->list:
    """
    -Funcion
    devuelve una lista con los totales de cada fila de la matriz "ventas"

    -Parametros
    "ventas" : matriz con valores de venta por trimestre 

    -Procedimiento
    recorre ventas
    crea variable "total"
    recorre cada lista de ventas
    suma el valor encontrado a total
    agrega total a lista totales
    
    -Retorna la lista totales
    """
    totales = []
    for i in range(len(ventas)):
        total = 0
        for j in range(len(ventas[i])):
            total += ventas[i][j]
        totales.append(total)
    return totales

def ordenar_may_men_totales (productos :list, ventas: list)->None:
    """
    funcion que ordena de mayor a menor los productos segun el total de la suma de cada trimestere
    y los imprime en una tabla 
    
    -Parametros
    "productos" (list):lista de productos 
    "ventas" : matriz con valores de venta por trimestre

    -Retorno
    la funcion no retorna nada solo muestra por pantalla

    -Funcionamiento
    Calcula los totales por producto usando "calcular_totales"
    Internamente hace una copia de los datos para no modificar las listas originales
    Busca el valor mas alto en la copia de totales 
    guarda su id(ubicacion) e imprime por pantalla los datos usando esa ubicacion 
    elimina esa posicion de las listas copiadas para que no se repita y continua con la busqueda 

    """
    totales = calcular_totales(ventas)
    prod_copia = []
    vent_copia = []
    tot_copia = []

    for i in range(len(productos)):
        prod_copia.append(productos[i])
        vent_copia.append(ventas[i])
        tot_copia.append(totales[i])

    print('Producto | T1 | T2 | T3 | Totales')
    print('---------------------------------')
    while len(tot_copia) > 0:
        max_total = -1
        pos_max = -1
        for i in range(len(tot_copia)):
            if tot_copia[i] > max_total:
                max_total = tot_copia[i]
                pos_max = i
        print('   ', prod_copia[pos_max], '   |',vent_copia[pos_max][0], '|',vent_copia[pos_max][1], '|',vent_copia[pos_max][2], '|',max_total)

        prod_copia.pop(pos_max)
        vent_copia.pop(pos_max)
        tot_copia.pop(pos_max)
   
def buscar_producto (productos: list, ventas: list, producto: str)->None:
    """
    Muestra las ventas de los trimestres y el total de un producto
    específico.

     -Parametros
    "productos" (list):lista de productos 
    "ventas" : matriz con valores de venta por trimestre
    "producto" : nombre de el producto a buscar cargado por usuario en programa principal

    -Retorno
    imprime la fila correspondiente al producto 

    -Funcionamiento
    busca en la lista productos 
    compara cada valor de la lista con el producto ingresado para buscar
    imprime el producto con sus trimestres y el total utilizando la ubicacion 
    """
    print('Producto | T1 | T2 | T3 | Total')
    print('-------------------------------')
    for i in range(len(productos)):
        if productos[i] == producto:
            print ('   ',producto,'   |' ,ventas[i][0], '|' ,ventas[i][1],'|' ,ventas[i][2],'|' ,calcular_totales(ventas)[i])

def buscar_valor (productos:list, ventas:list,valor_buscado:int)->None:
    """
    busca un valor ingresado por el usuario en la matriz ventas y 
    mustra a que producto y trimestre pertenece en caso de no encontrarse se pregunta
    si desea continuar buscando un nuevo valor
    
    
     -Parametros
    "productos" :lista de productos 
    "ventas" : matriz con valores de venta por trimestre
    "valor_buscado" : valor numerico a encontrar en la matriz ventas

    -Retorno
    muestra por pantalla el trimestre y el producto al que pertenece dicho valor

    -Funcionamiento
    recorre la matriz ventas 
    compara cada valor de la matriz con el valor solicitado
    en caso de encontrarlo muestra a que producto y trimestre pertenece 
    en caso contrario se informa que no se encontro el valor y se pregunta si
    se desea continuar la busqueda con un nuevo valor

    """
    seguir = 's'
    buscando = valor_buscado
    while seguir == 's':
        bandera = 1 
        for i in range(len(ventas)):
            for j in range(len(ventas[i])):
                if ventas[i][j] == buscando:
                    print('---------------------')
                    print('Producto | Trimestre ')
                    trimestre = 0
                    if j == 0:
                        trimestre = 1
                    elif j == 1:
                        trimestre = 2
                    else:
                        trimestre = 3
                    print('   ',productos[i],'   |   ',trimestre)
                    bandera = '0'
                    seguir = 'n' 
        if bandera == 1:              
            seguir = input('valor no encontrado, desea continuar con la busqueda,("s")si ("n")no: ').lower()
            while seguir != 's' and seguir != 'n':
                seguir = input('desea continuar con la busqueda,("s")si ("n")no: ').lower()
        if seguir == 's':
            buscando = int(input('ingrese el nuevo valor que desea buscar: '))
            
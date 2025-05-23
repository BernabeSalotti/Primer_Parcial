def calcular_promedio(entrada: list, valor: int)->bool:
    respuesta = False
    suma = 0 
    contador = 0
    for i in range (len(entrada)):
        suma += entrada[i]
        contador += 1
    resultado = suma / contador
    if resultado > valor :
        respuesta = True
    return respuesta

entrada = [10,20,30,40]
valor = 24

if calcular_promedio(entrada, valor) == True:
    print('el promedio es mayor al valor ')
else : 
    print('el promedio no es mayor al valor')



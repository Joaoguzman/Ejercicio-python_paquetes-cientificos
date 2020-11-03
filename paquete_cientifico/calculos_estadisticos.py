import math

#funcion promedio de numeros
def promedio(lista_numeros):
    suma = 0
    total =  len(lista_numeros)
    for x in range(len(lista_numeros)):
        suma = suma + lista_numeros[x]
    return suma/total
#funcion que obtiene la mediana de una lista de numeros
def mediana(lista_numeros):
    n = len(lista_numeros)  
    ordenada = sorted(lista_numeros)
    if len(lista_numeros)%2 == 0:
        p_medio_lista = int(n/2)
        mediana = (ordenada[p_medio_lista-1] + ordenada[p_medio_lista])/ 2
        return mediana
    else:
        p_medio_lista = (n/2)
        mediana = (ordenada[int(p_medio_lista)])
        return mediana
    
#funcion varianza de una lista de numeros y el promedio
def varianza(lista_numeros,promedio):
    suma = 0
    for x in range(len(lista_numeros)):
        suma = suma + ((lista_numeros[x] - promedio)**2)
    return suma/len(lista_numeros)

#funcion que obtiene la desviacon estandar con el promedio y una lista de numeros
def desviacion_estandar(promedio, lista_numeros):
    suma = 0
    for x in range(len(lista_numeros)):
        suma = suma + ((lista_numeros[x] - promedio)**2)
        desviacion = suma / len(lista_numeros)
    return math.sqrt(desviacion)


if __name__ =="__main__":

    
    print(promedio([10,10,10]))
    print(mediana([7,9,8,10,12,11,5]))
    print(varianza([10,32,24,26,40,24], 26))
    print(desviacion_estandar(26,[10,32,24,26,40,24]))
import math

import math

#funcion que retorna area y perimetro de un circulo
def ap_circulo(radio):
    area_circulo= math.pi*radio**2
    perimetro=math.pi*2*radio
    return area_circulo, perimetro

#funcion area y perimetro de triangulo dada su base y altura
def ap_triangulo(base, altura):
    area_triangulo= base*altura/2
    perimetro=base*3
    return area_triangulo, perimetro

#funcion area y perimetro de rectangulo dado sus lados
def ap_rectangulo (largo, ancho):
    area_rectangulo= largo*ancho
    perimetro= (largo+ancho)*2
    return area_rectangulo, perimetro

#funcion distancia recorrida, dados tiempo y velocidad
def distancia(tiempo, velocidad):
    distancia=tiempo*velocidad
    return distancia


if __name__ == "__main__":
    area, perimetro= ap_circulo(5)   
    print(area, perimetro)

    print(ap_triangulo(11,7))

    print(ap_rectangulo(10,5))

    print (distancia(1,100))

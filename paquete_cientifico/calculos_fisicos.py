import math

#funcion que calcula la equivalencia entre masa y energia
def mc2(m):
    c=3*(10**8)
    E=m*(c**2)
    return E

#funcion que calcula la densidad
def densidad (masa, volumen):
    densidad=masa/volumen
    return densidad

#funcion que calcula la fuerza

def fuerza(masa, aceleracion):
    fuerza=masa*aceleracion
    return fuerza

#funcion que calcula trabajo fisico

def trabajo_fisico(fuerza, densidad):
    trabajo_fisico=fuerza*densidad
    return trabajo_fisico    
   

if __name__ == "__main__":
    
    print(densidad(7,8))

    print(fuerza(70,5))

    print(trabajo_fisico(300,100))
    
    print(mc2(80))

    



    
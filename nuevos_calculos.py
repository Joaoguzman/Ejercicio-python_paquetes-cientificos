import math

def ap_circulo(radio):
    area_circulo=math.pi*radio**2
    perimetro_circulo=2*math.pi*radio
    print(f'El area del circulo es {area_circulo}')
    print(f'El perimetro del circulo es: {perimetro_circulo}')

ap_circulo(float(input("Inserte el radio del circulo: ")))

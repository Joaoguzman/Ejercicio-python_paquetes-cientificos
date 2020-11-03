import paquete_cientifico

energia = paquete_cientifico.mc2(50)
print("La energía es: ", energia)

densidad_fisica1 = paquete_cientifico.densidad_fisica(100, 50)
print("La densidad fisica es: ", densidad_fisica1)

trabajo = paquete_cientifico.trabajo_fisico(200, 200)
print("El trabajo es: ", trabajo)

fuerza = paquete_cientifico.fuerza(50, 50)
print("La fuerza es de: ", fuerza)

densidad_quimica1 = paquete_cientifico.densidad_quimica(50, 50)
print("La densidad química es: ", densidad_quimica1)

resultado_molaridad = paquete_cientifico.molaridad(100, 300)
print("La molaridad es de: ", resultado_molaridad)

resultado_molalidad = paquete_cientifico.molalidad(30, 50)
print("La molalidad es de: ", resultado_molalidad)

resultado_normalidad = paquete_cientifico.normalidad(100, 300)
print("La normalidad es de: ", resultado_normalidad)

promedio = paquete_cientifico.promedio([10,20,30])
print("El promedio es: ", promedio)

resultado_mediana = paquete_cientifico.mediana([7,9,8,10,12,11,5])
print("La mediana es: ", resultado_mediana)

resultado_varianza = paquete_cientifico.varianza([10,32,24,26,40,24], 26)
print("La varianza es: ", resultado_varianza)

resultado_sd = paquete_cientifico.desviacion_estandar(26,[10,32,24,26,40,24])
print("La desviacion estándar es: ", resultado_sd)
#funcion molaridad
def molaridad(moles, volumen_disolucion):
    molar=moles/volumen_disolucion
    return molar

#funcion molalidad
def molalidad(moles, litros_solvente):
    molal=moles/litros_solvente
    return molal

#funcion molaridad
def normalidad(equivalentes, litros_solvente1):
    n=equivalentes*litros_solvente1
    return n

#funcion densidad quimica
def densidad(gramos_disolucion, litros_disolucion):
    d=gramos_disolucion/litros_disolucion
    return d

if __name__ == "__main__":
    print("Molaridad es igual a: ", molaridad(30, 100))
    print("Molalidad es igual a: ", molalidad(60, 100))    
    print("Normalidad es igual a: ", normalidad(1000, 100))
    print("Densidad es igual a: ", densidad(25, 100))

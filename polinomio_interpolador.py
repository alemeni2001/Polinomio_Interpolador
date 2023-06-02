import numpy as np

# Obtengo los datos por el usuario que cota inferior, superior quiero y la cantidad de par de numeros

def ingresar_datos():
    cota_inferior = float(input("Ingresa la cota inferior para x: "))
    cota_superior = float(input("Ingresa la cota superior para x: "))
    cantidad = int(input("Ingresa la cantidad de pares de números: "))
    return cota_inferior, cota_superior, cantidad

# Funcion que genera segun una cantidad pares alaeatorios utilizando una cota superior e inferior, devuelve los pares x e y
def generar_pares_aleatorios(cota_inferior, cota_superior, cantidad):
    # Con la funcion random, le doy una "semilla" (esto es de forma arbitraria, el valor 10)
    np.random.seed(10)
    # Genero los valores de x
    x = np.random.uniform(cota_inferior, cota_superior, cantidad)
    # Los ordeno
    x.sort()
    # Genero los valores de y
    y = np.random.uniform(cota_inferior, cota_superior, cantidad)
    return x, y

def main():

    cota_inferior, cota_superior, cantidad = ingresar_datos()
    # Generar los pares de números aleatorios
    x, y = generar_pares_aleatorios(cota_inferior, cota_superior, cantidad)

    # Imprime valores
    print("Valores de x:", x)
    print("Valores de y:", y)


main()
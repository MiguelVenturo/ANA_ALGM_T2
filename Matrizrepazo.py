import random
import math
print("-----> BIENVENIDOS AL MATRIZ DE COORDENADAS <-----")
def generar_coordenadas(n):
    return [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(n)]
def distancia(coord):
    return math.sqrt(math.pow(coord[0],2) + math.pow(coord[1],2))
def max_distancia_divide_y_venceras(coordenadas, inicio, fin):
    if inicio == fin:
        coord = coordenadas[inicio]
        if coord[0] > 0 and coord[1] < 0:
            return coord
        else:
            return None
    medio = (inicio + fin) // 2
    izquierda = max_distancia_divide_y_venceras(coordenadas, inicio, medio)
    derecha = max_distancia_divide_y_venceras(coordenadas, medio + 1, fin)
    if izquierda is None:
        return derecha
    if derecha is None:
        return izquierda
    
    if distancia(izquierda) >= distancia(derecha):
        return izquierda
    else:
        return derecha
n = int(input("Ingrese la cantidad de pares de coordenadas: "))
coordenadas = generar_coordenadas(n)
print("\nCoordenadas generadas:")
print(coordenadas)

resultado = max_distancia_divide_y_venceras(coordenadas, 0, n - 1)
if resultado:
    print(f"\nLa coordenada más alejada del origen en el cuadrante IV es: {resultado} con distancia {distancia(resultado):.2f}")
else:
    print("\nNo se encontró ninguna coordenada en el cuadrante IV (X > 0, Y < 0).")
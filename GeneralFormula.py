import math

a = float(input("Introduzca el valor de A: ")) # Coeficiente al cuadrado
b = float(input("Introduzca el valor de B: ")) # Coeficiente linel
c = float(input("Introduzca el valor de C: ")) # Coeficiente independiente

if a != 0 and (math.pow(b, 2) > (4 * a * c)):
    d = math.sqrt(math.pow(b, 2) - 4 * a * c)

    x1 = (-b + d) / (2 * a)
    x2 = (-b - d) / (2 * a)
        
    print("La raíz de X1: ", x1)
    print("La raíz de x2: ", x2)
else:
    print("No es posible realizar la operación")
"""
Ejercicio #1
Para resolver este programa se requiere de:

Declarar las bibliotecas necesarias:
Se utiliza la biblioteca math para calcular la raíz cuadrada, math.sqrt()
Realizar la lectura de los datos de entrada (a, b y c)
Realizar el cálculo de  x 
Mostrar el resultado
Crear la expresión en Python que resuelvan la siguiente fórmula:

x=b−a2−−−−−√c 

Los valores de a,b y c deberán ser introducidos desde el teclado

Caso de prueba
a = 2
b = 20
c = 5
por lo tanto x = 0.8
"""
#problema: calcular el valor de x a partir de los valores de a, b y c
#ENTRADAS: a, b, c
#SALIDAS: x
#ALGORITMO:
#1. Leer los valores de a, b y c
#2. Calcular el valor de x utilizando la fórmula x = (b - a) / (2 * sqrt(c))
#3. Mostrar el resultado de x

#CONTRATO DE FUNCIONES
#leerDatos()
#Entradas: Ninguna
#Responsabilidad: Leer los valores de a, b y c desde el teclado


#calcularX(a, b, c)
#Entradas: a, b, c
#Salidas: x
#Responsabilidad: Calcular el valor de x utilizando la fórmula x = sqrt(b-a**2)/c

#MostrarResultado(x)
#Entradas: x
#Salida: Ninguna
#Responsabilidad: Mostrar el resultado de x

#CASOS DE PRUEBA
#Caso 1
#Entradas: a = 2, b = 20, c = 5
#Salidas: x = 0.8
#Caso 2
#Entradas: a = 5, b = 15, c = 10
#Salidas: x = 0.5

#Restricciones
#1. Los valores de a, b y c deben ser números reales.
#2. El valor de c no puede ser cero, ya que causaría una división por cero.
#3. Los valores de a, b y c deben ser ingresados por el usuario desde el teclado.

def leerDatos():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c

def calcularX(a, b, c):
    import math
    x = math.sqrt(b - a**2) / c
    return xS
   
 

def mostrarResultado(x):
    print("El valor de x es:", x)

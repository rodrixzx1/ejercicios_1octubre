"""
Ejercicio #2
Para resolver este programa se requiere de:

Declarar las bibliotecas necesarias:
Se utiliza la biblioteca math para calcular la raíz cuadrada, recuperar el valor de Euler (e) y recuperar el valor de pi, math.sqrt(), math.e y math.pi
Realizar la lectura de los datos de entrada (n)
Realizar el cálculo de  n! 
Mostrar el resultado
Crear la expresión en Python que resuelvan la siguiente fórmula:

n!≈2π−−√e−nnn+12 

El valor de n deberá ser introducido desde el teclado

Caso de prueba
n = 5
por lo tanto n! = 118.019168
"""
#problema: calcular la aproximación de n! utilizando la fórmula de Stirling
#ENTRADAS: n
#SALIDAS: resultado (n!)
#ALGORITMO:
#1. Leer el valor de n ingresado por el teclado
#2. Calcular el valor de la aproximación utilizando la fórmula math.sqrt(2 * math.pi) * (math.e ** -n) * (n ** (n + 0.5))
#3. Mostrar el resultado obtenido de n!

#CONTRATO DE FUNCIONES
#leerDatos()
#Entradas: Ninguna
#Responsabilidad: Leer el valor de n desde el teclado

#calcularFactorialAprox(n)
#Entradas: n
#Salidas: resultado
#Responsabilidad: Calcular el valor de n! utilizando las funciones math.sqrt(), math.e y math.pi

#MostrarResultado(resultado)
#Entradas: resultado
#Salida: Ninguna
#Responsabilidad: Mostrar el resultado final de n!

#CASOS DE PRUEBA
#Caso 1
#Entradas: n = 5
#Salidas: n! = 118.019168

#Restricciones
#1. Se requiere declarar e importar la biblioteca math para utilizar la raíz cuadrada, el valor de Euler (e) y pi.
#2. El valor de n deberá ser introducido obligatoriamente desde el teclado.

def leerDatos():
    n = int(input("Ingrese el valor de n: "))
    return n

def calcularFactorialAprox(n):
    import math
    resultado = math.sqrt(2 * math.pi) * (math.e ** -n) * (n ** (n + 0.5))
    return resultado

def mostrarResultado(resultado):
    print("El valor aproximado de n! es:", resultado)



from Soluciones.Ejercicio_1 import leerDatos, calcularX, mostrarResultado
from Soluciones.Ejercicio_2 import leerDatos as leerDatos2, calcularFactorialAprox, mostrarResultado as mostrarResultado2

def main():
    while True:
        print("Menú de opciones:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            a, b, c = leerDatos()
            x = calcularX(a, b, c)
            mostrarResultado(x)
        elif opcion == "2":
            n = leerDatos2()
            resultado = calcularFactorialAprox(n)
            mostrarResultado2(resultado)
    
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
    
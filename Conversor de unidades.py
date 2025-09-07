import math

# Funciones de conversiones
def convertir_longitud(metros):
    centimetros = metros * 100
    kilometros = metros / 1000
    return f"{metros} metros son {centimetros} cm y {kilometros} km"

def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius} °C son {fahrenheit} °F"

# Funciones de operaciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir entre 0"
    return (f"Suma: {suma}\n"
            f"Resta: {resta}\n"
            f"Multiplicación: {multiplicacion}\n"
            f"División: {division}")

def calcular_potencia(base, exponente):
    resultado = math.pow(base, exponente)
    return f"{base}^{exponente} = {resultado}"

# Menú principal
def main():
    print("Bienvenido al programa de Conversiones y Operaciones Básicas")

    print("\nSelecciona una opción:")
    print("1. Conversión de longitud (m a cm y km)")
    print("2. Conversión de temperatura (°C a °F)")
    print("3. Operaciones básicas (suma, resta, multiplicación, división)")
    print("4. Potencia (elevar un número)")
    print("5. Salir") 

    opcion = int(input("Escribe tu opción: "))

    if opcion == 1:
        metros = float(input("Ingresa los metros: "))
        print(convertir_longitud(metros))

    elif opcion == 2:
        celsius = float(input("Ingresa la temperatura en °C: "))
        print(convertir_temperatura(celsius))

    elif opcion == 3:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(operaciones_basicas(a, b))

    elif opcion == 4:
        base = float(input("Base: "))
        exponente = float(input("Exponente: "))
        print(calcular_potencia(base, exponente))

    elif opcion == 5:
        print("Gracias por usar el programa. ¡Hasta luego!")

    else:
        print("Opción no válida.")

# Ejecutar el programa
main()
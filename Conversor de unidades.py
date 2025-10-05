import math

# Funciones de conversiones
def convertir_longitud(metros):
    conversiones = [("centímetros", metros * 100), ("kilómetros", metros / 1000)]
    print(f"\n{metros} metros equivalen a:")
    for unidad, valor in conversiones:
        print(f"- {valor} {unidad}")

def convertir_temperatura(celsius):
    conversiones = [("Fahrenheit", (celsius * 9/5) + 32)]
    print(f"\n{celsius} °C equivalen a:")
    for unidad, valor in conversiones:
        print(f"- {valor} °{unidad[0]}")

# Funciones de operaciones
def operaciones_basicas(a, b):
    operaciones = [
        ("Suma", a + b),
        ("Resta", a - b),
        ("Multiplicación", a * b),
        ("División", "No se puede dividir entre 0" if b == 0 else a / b)
    ]

    print("\nResultados de las operaciones:")
    for nombre, resultado in operaciones:
        print(f"- {nombre}: {resultado}")

def calcular_potencia(base, exponente):
    resultado = math.pow(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}")

# Menú principal con ciclo y uso de listas
def main():
    print("Bienvenido al programa de Conversiones y Operaciones Básicas")

    opciones = [
        "Conversión de longitud (m a cm y km)",
        "Conversión de temperatura (°C a °F)",
        "Operaciones básicas (suma, resta, multiplicación, división)",
        "Potencia (elevar un número)",
        "Salir"
    ]

    opcion = 0
    while opcion != 5:
        print("\nSelecciona una opción:")
        for i in range(len(opciones)):
            print(f"{i+1}. {opciones[i]}")

        opcion = int(input("Escribe tu opción: "))

        if opcion == 1:
            metros = float(input("Ingresa los metros: "))
            convertir_longitud(metros)

        elif opcion == 2:
            celsius = float(input("Ingresa la temperatura en °C: "))
            convertir_temperatura(celsius)

        elif opcion == 3:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            operaciones_basicas(a, b)

        elif opcion == 4:
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            calcular_potencia(base, exponente)

        elif opcion == 5:
            print("Gracias por usar el programa. ¡Hasta luego!")

        else:
            print("Opción no válida.")

# Ejecutar el programa
main() 
import math


def convertir_longitud(metros):
    """Convierte una longitud en metros a centímetros y kilómetros."""
    conversiones = [("centímetros", metros * 100),
                    ("kilómetros", metros / 1000)]
    print(f"\n{metros} metros equivalen a:")
    for unidad, valor in conversiones:
        print(f"- {valor} {unidad}")


def convertir_temperatura(celsius):
    """Convierte una temperatura en grados Celsius a Fahrenheit."""
    conversiones = [("Fahrenheit", (celsius * 9 / 5) + 32)]
    print(f"\n{celsius} °C equivalen a:")
    for unidad, valor in conversiones:
        print(f"- {valor} °{unidad[0]}")


def operaciones_basicas(a, b):
    """Realiza operaciones básicas: suma, resta, multiplicación y división."""
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
    """Calcula la potencia de un número elevado a un exponente.

    Utiliza la función math.pow() del módulo math del API de Python.
    """
    resultado = math.pow(base, exponente)
    print(f"\n{base}^{exponente} = {resultado}")


def main():
    """Muestra un menú para realizar conversiones y operaciones básicas."""
    print("Bienvenido al programa de Conversiones y Operaciones Básicas")
    opciones = [
        "Conversión de longitud (m a cm y km)",
        "Conversión de temperatura (°C a °F)",
        "Operaciones básicas (suma, resta, multiplicación, división)",
        "Potencia (elevar un número)",
        "Ver historial",
        "Salir"
    ]
    historial = []
    opcion = 0

    while opcion != 6:
        print("\n==============================")
        print("Selecciona una opción:")
        for i in range(len(opciones)):
            print(f"{i + 1}. {opciones[i]}")
        print("==============================")

        opcion = int(input("Escribe tu opción: "))

        if opcion == 1:
            metros = float(input("Ingresa los metros: "))
            resultado = (
                f"{metros} m -> {metros * 100} cm y {metros / 1000} km"
            )
            convertir_longitud(metros)
            historial.append(["Conversión de longitud", resultado])

        elif opcion == 2:
            celsius = float(input("Ingresa la temperatura en °C: "))
            resultado = f"{celsius} °C -> {(celsius * 9 / 5) + 32} °F"
            convertir_temperatura(celsius)
            historial.append(["Conversión de temperatura", resultado])

        elif opcion == 3:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            operaciones_basicas(a, b)
            historial.append(["Operaciones básicas", f"Números: {a}, {b}"])

        elif opcion == 4:
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            calcular_potencia(base, exponente)
            historial.append(["Potencia", f"{base}^{exponente}"])

        elif opcion == 5:
            if len(historial) == 0:
                print("\nNo hay operaciones registradas aún.")
            else:
                print("\nHistorial de operaciones:")
                for registro in historial:
                    print(f"- {registro[0]} → {registro[1]}")

        elif opcion == 6:
            print("\nGracias por usar el programa. ¡Hasta luego!")

        else:
            print("\nOpción no válida.")

        if opcion != 6:
            input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    main()

# -------------------------------------------------------------
# Referencias al API de Python:
# - math.pow(x, y): Devuelve el resultado de elevar x a la potencia y.
#   https://docs.python.org/3/library/math.html#math.pow
# - print(): Función integrada que muestra texto en la consola.
#   https://docs.python.org/3/library/functions.html#print
# - input(): Lee una entrada del usuario desde la consola.
#   https://docs.python.org/3/library/functions.html#input
# - float(), int(): Convierte cadenas a números de punto flotante o enteros.
#   https://docs.python.org/3/library/functions.html#float
# -------------------------------------------------------------
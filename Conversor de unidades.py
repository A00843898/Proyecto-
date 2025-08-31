import math

print("Bienvenido al programa de Conversiones y Operaciones Básicas")

# Mostrar menú principal
print("\nSelecciona una opción:")
print("1. Conversión de longitud (metros a cm y km)")
print("2. Conversión de temperatura (°C a °F)")
print("3. Operaciones básicas (suma, resta, multiplicación, división)")
print("4. Potencia (elevar un número)")
print("5. Salir")

opcion = int(input("Ingresa el número de la opción: "))

# Opción 1: Longitud
if opcion == 1:
    metros = float(input("Ingresa el valor en metros: "))
    centimetros = metros * 100   # multiplicación
    kilometros = metros / 1000   # división
    print(f"{metros} metros equivalen a {centimetros} cm y {kilometros} km")

# Opción 2: Temperatura
else:
    if opcion == 2:
        celsius = float(input("Ingresa la temperatura en °C: "))
        fahrenheit = (celsius * 9/5) + 32   # multiplicación, división y suma
        print(f"{celsius} °C equivalen a {fahrenheit} °F")
    else:
        # Opción 3: Operaciones básicas
        if opcion == 3:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            suma = a + b
            resta = a - b
            multiplicacion = a * b
            division = a / b
            print(f"Suma: {a} + {b} = {suma}")
            print(f"Resta: {a} - {b} = {resta}")
            print(f"Multiplicación: {a} * {b} = {multiplicacion}")
            print(f"División: {a} / {b} = {division}")
        else:
            # Opción 4: Potencia
            if opcion == 4:
                base = float(input("Ingresa la base: "))
                exponente = float(input("Ingresa el exponente: "))
                potencia = math.pow(base, exponente)
                print(f"{base} ^ {exponente} = {potencia}")
            else:
                # Opción 5: Salir
                if opcion == 5:
                    print("Gracias por usar el programa. ¡Hasta luego!")
                else:
                    print("Opción no válida, por favor intenta de nuevo.")
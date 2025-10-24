# Proyecto-
Conversor de unidades

Este proyecto consiste en un conversor de múltiples unidades. El objetivo es crear un programa que permita realizar conversiones básicas en diferentes categorías como longitud, masa, temperatura y divisas.
Elegí este tema porque me parece práctico y útil, ya que las conversiones de unidades se usan en la vida diaria y en muchas áreas de estudio como las matemáticas, la física y la ingeniería. Además, es un proyecto que se puede empezar con lo básico (menús, operaciones matemáticas y ciclos) y al mismo tiempo ofrece la posibilidad de agregar más funciones conforme vaya avanzando el semestre, lo cual lo hace interesante y un buen reto.


Pseudocodigo

Entradas:
opción (entero)
metros (real)
celsius (real)
a, b (reales)
base, exponente (enteros o reales)

Proceso:
Inicio
Mostrar mensaje "Bienvenido al programa de Conversiones y Operaciones Básicas"

Mostrar menú de opciones:
 1. Conversión de longitud
 2. Conversión de temperatura
 3. Operaciones básicas
 4. Potencia
 5. Ver historial
 6. Salir

Leer opcion

Mientras opcion ≠ 6 hacer:
 5.1. Si opcion = 1 entonces
   Leer metros
   Calcular centimetros = metros * 100
   Calcular kilometros = metros / 1000
   Mostrar "Centímetros: ", centimetros
   Mostrar "Kilómetros: ", kilometros
   Guardar resultado en historial
 5.2. Si opcion = 2 entonces
   Leer celsius
   Calcular fahrenheit = (celsius * 9 / 5) + 32
   Mostrar "Temperatura en Fahrenheit: ", fahrenheit
   Guardar resultado en historial
 5.3. Si opcion = 3 entonces
   Leer a y b
   Calcular suma = a + b
   Calcular resta = a - b
   Calcular multiplicacion = a * b
   Si b ≠ 0 entonces
    Calcular division = a / b
   Si no
    Mostrar "No se puede dividir entre 0"
   FinSi
   Mostrar todos los resultados
   Guardar operación en historial
 5.4. Si opcion = 4 entonces
   Leer base y exponente
   Calcular resultado = base ^ exponente
   Mostrar "Resultado: ", resultado
   Guardar operación en historial
 5.5. Si opcion = 5 entonces
   Si historial está vacío entonces
    Mostrar "No hay operaciones registradas aún"
   Si no
    Mostrar todos los elementos del historial
   FinSi
 5.6. Si opcion no está entre 1 y 6 entonces
   Mostrar "Opción no válida"
 5.7. Mostrar menú nuevamente
 5.8. Leer nueva opcion

Mostrar "Gracias por usar el programa"

Fin del programa

Salidas:

Resultados de conversiones y operaciones matemáticas

Historial de acciones realizadas

Mensaje de despedida

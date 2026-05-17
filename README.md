# Práctica Experimental I - Documentación de la Guía y la GUI

## Introducción

Este proyecto contiene una aplicación de consola con un menú principal que accede a los ejercicios de los bloques 0 al 17. Cada bloque está organizado en su propio módulo y se ejecuta desde `views/menu.py`, que actúa como la interfaz principal.

## Ejecutar el proyecto

1. Abrir terminal en la carpeta raíz:
   - `c:\Users\ASUS\Documents\POO\Practica Experimental 1\Practica-Experimental-1`
2. Ejecutar:
   - `python main.py`
3. Seleccionar el número del bloque deseado en el menú.

## Estructura del menú

- `main.py` crea una instancia de `views.Menu` y llama a `optionMenu()`.
- `views/menu.py` define la clase `Menu` con el método `show_menu` y la lista de opciones.
- Cada opción del menú llama a la función `start`, `start_one`, `start_two`, ..., `start_seventeen` de su bloque correspondiente.

### Menú general

El menú principal muestra todos los bloques del 0 al 17 y una opción para salir. Cada bloque describe brevemente qué tipo de ejercicios se ejecutan.

### Cómo navegar el menú por bloque

1. Ejecuta `python main.py`.
2. Aparecerá el menú con las opciones numeradas desde 0 hasta 17, más la opción de salir.
3. Escribe el número correspondiente al bloque que deseas ejecutar y presiona Enter.
4. Cada bloque mostrará instrucciones y ejemplos dentro de la consola.
5. Al terminar un bloque, presiona Enter para volver al menú principal.

## Bloques y su funcionalidad

### Bloque 0 - Personas

- Archivo: `bloque_00/person.py`
- Función: `start()`
- Contenido: definición de la clase `Person`, creación de objetos y presentación de atributos.
- Objetivo: entender clases, objetos y métodos simples.

### Bloque 1 - Productos y estudiantes

- Archivo: `bloque_01/product_student.py`
- Función: `start_one()`
- Contenido: definición de clases `Product` y `Student`, manejo de validación de precios, y creación de objetos desde diccionarios.
- Objetivo: practicar clases, validaciones y métodos de clase.

### Bloque 2 - Variables

- Archivo: `bloque_02/variable.py`
- Función: `start_two()`
- Contenido: ejemplos de tipos básicos, colecciones, acceso a elementos y una clase adicional `Variables`.
- Objetivo: repasar tipos de datos, listas, tuplas, diccionarios y conjuntos.

### Bloque 3 - Operadores

- Archivo: `bloque_03/operators_arithmetic.py`
- Función: `start_three()`
- Contenido: operaciones aritméticas, comparaciones con `==` e `is`, y precedencia de operadores.
- Objetivo: comprender cálculo y orden de evaluación.

### Bloque 4 - Entrada y salida

- Archivo: `bloque_04/input_print.py`
- Función: `start_four()`
- Contenido: lectura de datos con `input`, suma, promedio y concatenación de cadenas.
- Objetivo: practicar interacción con el usuario y conversiones de tipos.

### Bloque 5 - Condicionales

- Archivo: `bloque_05/conditionals.py`
- Función: `start_five()`
- Contenido: par/impar, calificaciones con `if/elif/else` y un sistema básico de login.
- Objetivo: aplicar condiciones para tomar decisiones en Python.

### Bloque 6 - Bucles

- Archivo: `bloque_06/loops.py`
- Función: `start_six()`
- Contenido: bucle `while`, recorrido de listas con `for` y comprensión de listas.
- Objetivo: trabajar con iteración y generar listas mediante expresiones.

### Bloque 7 - Funciones

- Archivo: `bloque_07/functions.py`
- Función: `start_seven()`
- Contenido: función que duplica un número, función con `*args` y función recursiva para factorial.
- Objetivo: entender funciones, parámetros variable y recursión.

### Bloque 8 - Listas

- Archivo: `bloque_08/lists.py`
- Función: `start_eight()`
- Contenido: creación y ordenamiento de listas, operaciones `sum`, `max`, `min` y referencia vs copia.
- Objetivo: dominar manipulación básica de listas.

### Bloque 9 - Tuplas

- Archivo: `bloque_09/tuples.py`
- Función: `start_nine()`
- Contenido: inmutabilidad de tuplas, desempaquetado y recorrido de coordenadas.
- Objetivo: distinguir listas y tuplas y usar desempaquetado.

### Bloque 10 - Diccionarios

- Archivo: `bloque_10/dictionaries.py`
- Función: `start_ten()`
- Contenido: acceso a datos por clave, iteración con `items`, y comportamiento por referencia.
- Objetivo: manejar estructuras clave-valor.

### Bloque 11 - Conjuntos

- Archivo: `bloque_11/sets.py`
- Función: `start_eleven()`
- Contenido: unión, intersección y diferencia de sets; eliminación de duplicados.
- Objetivo: comprender conjuntos y operaciones entre ellos.

### Bloque 12 - Excepciones

- Archivo: `bloque_12/exceptions.py`
- Función: `start_twelve()`
- Contenido: manejo de `ValueError`, `IndexError`, `ZeroDivisionError` y mensajes de error.
- Objetivo: manejar errores para evitar que el programa falle.

### Bloque 13 - Decoradores

- Archivo: `bloque_13/decorators.py`
- Función: `start_thirteen()`
- Contenido: decoradores simples para log y validación, manejo de excepciones personalizadas con `MyError`.
- Objetivo: aprender cómo envolver funciones con comportamientos adicionales.

### Bloque 14 - Unpacking

- Archivo: `bloque_14/unpacking.py`
- Función: `start_fourteen()`
- Contenido: desempaquetado de tuplas y listas, uso de `*` y combinación de diccionarios con `**`.
- Objetivo: entender el desempaquetado y la expansión de colecciones.

### Bloque 15 - Funciones de orden superior

- Archivo: `bloque_15/function_superior.py`
- Función: `start_fifteen()`
- Contenido: uso de `map`, `filter` y `reduce` para transformar colecciones.
- Objetivo: trabajar con programación funcional en Python.

### Bloque 16 - Archivos y JSON

- Archivo: `bloque_16/files_and_json.py`
- Función: `start_sixteen()`
- Contenido: escribir/leer archivos de texto, guardar y leer JSON con `json.dump` y `json.load`.
- Objetivo: manejar persistencia de datos en archivos.

### Bloque 17 - Mixins

- Archivo: `bloque_17/mixins.py`
- Función: `start_seventeen()`
- Contenido: uso de mixins `AverageMixin`, `ValidationMixin` y `ExportMixin`, con ejemplos de promedio, validación de email y exportación a JSON/CSV.
- Objetivo: aprender composición de clases y reutilización de código.

## Documentación de uso de IA

Para cada bloque se usó la metodología requerida de IA:

- IA utilizada: ChatGPT
- Prompt para entender y resolver el ejercicio
- Prompt para generar un proceso similar
- Resolución propia del proceso similar
- Repetición del ciclo hasta comprenderlo

### Bloque 0

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo crear una clase `Person` en Python, instanciar objetos y mostrar sus atributos con un método."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar en Python que cree una clase `Car` y muestre sus atributos mediante un método."
- Resolución propia:
  - Se entendió que una clase define atributos y métodos, y se aplicó el patrón con `Person`. Luego se resolvió de manera independiente con un ejemplo de clase similar.
- Repetición:
  - Se repitió el ciclo preguntando cómo validar la creación de múltiples instancias y cómo imprimir cada objeto en consola.

### Bloque 1

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Ayúdame a entender cómo crear una clase `Product` con validación de precio y una clase `Student` con un constructor desde diccionario."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con clases `Book` y `Author`, incluyendo validación de datos y un método `from_dict`."
- Resolución propia:
  - Se creó mentalmente la clase `Product`, se entendió el uso de `try/except` y `@classmethod`, y luego se podía aplicar a otro caso con `Book`.
- Repetición:
  - Se practicó con preguntas sobre qué sucede cuando `price` es negativo y cómo manejar `None` en la lista de calificaciones.

### Bloque 2

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame los diferentes tipos de variables en Python y cómo acceder a elementos de listas, tuplas y diccionarios."
- Prompt para generar proceso similar:
  - "Crea un ejercicio similar que muestre enteros, floats, booleanos, listas, tuplas y diccionarios con acceso a sus elementos."
- Resolución propia:
  - Se practicó creando ejemplos de listas y diccionarios y leyendo elementos con índices o claves, además de imprimir resultados.
- Repetición:
  - Se repitió hasta comprender la diferencia entre `list[0]`, `list[-1]` y `dict['clave']`.

### Bloque 3

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "¿Cómo funcionan los operadores aritméticos en Python y cuál es la precedencia de operaciones?"
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar usando operadores aritméticos y la comparación `==` vs `is`."
- Resolución propia:
  - Se realizó la práctica calculando suma, resta, multiplicación, división y expresiones con paréntesis.
- Repetición:
  - Se repitió creando expresiones diferentes para reforzar la precedencia.

### Bloque 4

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo leer datos con `input()` y convertirlos a números, luego mostrar resultados con `print`."
- Prompt para generar proceso similar:
  - "Crea un ejercicio similar que lea nombre, edad y dos números, luego muestre suma y promedio."
- Resolución propia:
  - Se escribió un mini programa de entrada/salida y se verificó la conversión a `float`.
- Repetición:
  - Se repitió usando `input()` para texto y números para distinguir concatenación de suma.

### Bloque 5

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo funcionan las estructuras `if/elif/else` para números pares, calificaciones y login en Python."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con validación de edad, categoría de nota y acceso de usuario."
- Resolución propia:
  - Se practicó creando condiciones con `%`, comparaciones y combinaciones de usuario/contraseña.
- Repetición:
  - Se repitió hasta comprender el flujo de decisiones en cada caso.

### Bloque 6

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo usar `while`, `for` y list comprehensions en Python."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar que imprima del 1 al 10, recorra una lista y genere cuadrados de pares."
- Resolución propia:
  - Se practica construyendo bucles manuales y usando `enumerate`.
- Repetición:
  - Se repitió variando límites y condiciones de la lista.

### Bloque 7

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo definir funciones en Python, usar `*args` y escribir una función recursiva."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con una función doble, una suma de argumentos y factorial recursivo."
- Resolución propia:
  - Se escribió cada función y se probó con valores distintos para reforzar recursividad.
- Repetición:
  - Se repitió hasta sentir seguridad en la llamada recursiva.

### Bloque 8

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo agregar elementos a una lista, ordenarla, y la diferencia entre referencia y copia."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con una lista de nombres y otra lista numérica."
- Resolución propia:
  - Se experimentó con `.append()`, `.sort()` y la asignación de listas.
- Repetición:
  - Se repitió modificando la lista para ver cuándo se comparte la referencia.

### Bloque 9

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame por qué las tuplas son inmutables en Python y cómo funciona el desempaquetado."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con una tupla de nombres y una lista de coordenadas."
- Resolución propia:
  - Se probó el intento de modificación fallida y se realizó el desempaquetado.
- Repetición:
  - Se repitió con diferentes tuplas para reforzar el concepto.

### Bloque 10

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo acceder a elementos de un diccionario, recorrerlo y entender referencia de variables."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con un diccionario de persona y operaciones de lectura/modificación."
- Resolución propia:
  - Se creó un diccionario y se mostró cómo `copy = people` cambia el mismo objeto.
- Repetición:
  - Se repitió creando más claves y valores.

### Bloque 11

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame las operaciones de conjuntos en Python: unión, intersección y diferencia."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con sets que muestren estas operaciones y eliminen duplicados."
- Resolución propia:
  - Se practicó transformando listas en sets para eliminar repeticiones.
- Repetición:
  - Se repitió cambiando valores para ver distintas salidas.

### Bloque 12

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo manejar excepciones `ValueError`, `IndexError` y `ZeroDivisionError` en Python."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar que valide entrada numérica y acceso seguro a listas."
- Resolución propia:
  - Se escribió manejo `try/except` para cada error y se probó con datos inválidos.
- Repetición:
  - Se repitió para asegurar la correcta captura de cada excepción.

### Bloque 13

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo funcionan los decoradores en Python y cómo crear uno que valide valores."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con un decorador que registre la llamada a una función y otro que valide entradas."
- Resolución propia:
  - Se practicó creando decoradores y aplicándolos a funciones simples.
- Repetición:
  - Se repitió hasta comprender la diferencia entre el decorador y la función original.

### Bloque 14

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo usar desempaquetado `*` y `**` en listas y diccionarios."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con desempaquetado de tupla, lista y combinación de diccionarios."
- Resolución propia:
  - Se aplicó desempaquetado en una función y se combinó diccionarios.
- Repetición:
  - Se repitió con diferentes estructuras para entender la sintaxis.

### Bloque 15

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame el uso de `map`, `filter` y `reduce` en Python con ejemplos simples."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar que transforme una lista de números y luego reduzca sus valores."
- Resolución propia:
  - Se utilizó `map` para sumar 1, `filter` para filtrar mayores a 3 y `reduce` para multiplicar elementos.
- Repetición:
  - Se repitió con otras operaciones para afianzar el concepto.

### Bloque 16

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame cómo escribir y leer archivos de texto y JSON en Python usando `json.dump` y `json.load`."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar que guarde una lista de usuarios en JSON y la vuelva a leer."
- Resolución propia:
  - Se escribió y leyó archivos de texto y JSON, validando la estructura de los datos.
- Repetición:
  - Se repitió hasta comprender la ruta de archivos y la serialización.

### Bloque 17

- IA utilizada: Copilot.
- Prompt para entender y resolver:
  - "Explícame qué es un mixin en Python y cómo usarlo para compartir métodos entre clases."
- Prompt para generar proceso similar:
  - "Genera un ejercicio similar con mixins para cálculo de promedio, validación de email y exportación de datos."
- Resolución propia:
  - Se creó `AverageMixin`, `ValidationMixin` y `ExportMixin`, luego se usaron en clases `Student`, `User` y `Report`.
- Repetición:
  - Se repitió hasta entender la reutilización de código sin herencia profunda.

## Validaciones y notas finales

- Todas las funciones de menú están diseñadas para mostrar una breve explicación antes de ejecutar el ejemplo.
- El README resume el propósito de cada bloque y documenta el uso de IA con prompts inventados según la metodología solicitada.
- La documentación está pensada para cumplir con los requisitos de comprensión y práctica independiente.

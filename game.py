"""
a- Modifique el programa anterior con las siguientes funcionalidades:
El juego tiene un bug. Si no se inserta ninguna letra para adivinar, el valor de la
letra es un string vacío "". Para este caso, el juego marca como que es un acierto.
Modifica el mismo para que indique que es un error en este caso.

b- Modifique el juego para que en lugar de tener un número intentos se tenga un
número de fallos. En este caso el usuario pierde cuando el número de fallos es
alcanzado.

c- Agregue al juego niveles de dificultad. La variación de la dificultad sería:
    Fácil: En la palabra a adivinar se muestran todas las vocales por defecto.
    Media: Se muestra la primer y la última letra de la palabra.
    Difícil: No se muestra ninguna letra de la palabra.
Nota: Por cada funcionalidad agregada se debe realizar al menos un commit que identifique
el cambio.
"""

import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo",
         "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
max_attempts = 10

# Lista para almacenar las letras adivinadas
guessed_letters = []

# Mensaje de bienvenida
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

# Mostrar la palabra parcialmente adivinada
word_displayed = "_" * len(secret_word)
print(f"Palabra: {word_displayed}")

# Bucle principal del juego
for i in range(max_attempts):

    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Validar la entrada
    if not letter or len(letter) > 1:
        print("Error: Debes ingresar una letra.")
        continue

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)

    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break

# Mensaje de fin del juego
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
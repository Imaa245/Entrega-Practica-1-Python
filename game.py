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
max_attempts = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

# Mensaje de bienvenida
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
print(f"Solo puedes fallar {max_attempts} veces")

# Mostrar la palabra parcialmente adivinada
print("Modos: ")
print ("1: Fácil: En la palabra a adivinar se muestran todas las vocales por defecto.")
print ("2: Media: Se muestra la primer y la última letra de la palabra.")
print ("3: Difícil: No se muestra ninguna letra de la palabra.")
dificultad = int(input("Ingrese la dificultad (1 a 3): "))
aux = []
match (dificultad):
    case 1:
        for letra in secret_word:
            if letra in "aeiou":
                guessed_letters.append(letra)
                aux.append(letra)
            else:
                aux.append("_")
        word_displayed = "".join(aux)
    case 2:
        word_displayed = f"{secret_word[0]}{'_' * (len(secret_word) - 2)}{secret_word[-1]}"
        print("Ten en cuenta que a pesar de que la primer y última letra se hayan mostrado, se pueden repetir")
    case 3:
        word_displayed = "_" * len(secret_word)
print(f"Palabra: {word_displayed}")

# Bucle principal del juego
while True:

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
        max_attempts -= 1
        if (max_attempts > 0):
            print(f"Te quedan {max_attempts} intentos")
        else:
            # Mensaje de fin del juego
            print(f"¡Oh no! Has alcanzado el número de fallos permitido.")
            print(f"La palabra secreta era: {secret_word}")
            break

    # Mostrar la palabra parcialmente adivinada
    letters = []
    if (dificultad != 2):
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    else:
        for letter in secret_word[1:-1]:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = secret_word[0] + "".join(letters) + secret_word[-1]
    print(f"Palabra: {word_displayed}")
            

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
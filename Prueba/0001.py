import random

# Generar una cadena de números distintos
def generar_cadena(longitud):
    numeros = list(range(10))
    random.shuffle(numeros)
    cadena = ""
    for i in range(longitud):
        cadena += str(numeros[i])
    return cadena

# Contar cuántos números están en la posición correcta
def contar_aciertos(cadena_secreta, intento):
    aciertos = 0
    for i in range(len(cadena_secreta)):
        if cadena_secreta[i] == intento[i]:
            aciertos += 1
    return aciertos

# Función principal del juego
def jugar_master_mind():
    longitud = int(input("Dime la longitud de la cadena (de 2 a 9 cifras): "))
    
    cadena_secreta = generar_cadena(longitud)
    print("He generado una cadena de números distintos. ¡Intenta adivinarla!")

    while True:
        intento = input("Intenta adivinar la cadena: ")

        if len(intento) != longitud or not intento.isdigit() or len(set(intento)) != longitud:
            print(f"Por favor, ingresa una cadena de {longitud} cifras distintas.")
            continue

        aciertos = contar_aciertos(cadena_secreta, intento)
        print(f"Con {intento} has adivinado {aciertos} valores.")
        
        if aciertos == longitud:
            print("¡Felicidades! Has adivinado la cadena completa.")
            break

# Iniciar el juego
jugar_master_mind()


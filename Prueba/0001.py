import random

# Generar una cadena de números distintos
def generar_cadena(long):
    numeros = list(range(10))
    random.shuffle(numeros)
    cadena = ""
    for i in range(long):
        cadena += str(numeros[i])
    return cadena

# Contar cuántos números están en la posición correcta
def contar(numero_aleatorio, intento):
    aciertos = 0
    for i in range(len(numero_aleatorio)):
        if numero_aleatorio[i] == intento[i]:
            aciertos += 1
    return aciertos

# Función principal del juego
def jugar():
    long = int(input("Dime la long de la cadena (de 2 a 9 cifras): "))
    
    numero_aleatorio = generar_cadena(long)
    print("He generado una cadena de números distintos. ¡Intenta adivinarla!")

    while True:
        intento = input("Intenta adivinar la cadena: ")

        if len(intento) != long or not intento.isdigit() or len(set(intento)) != long:
            print(f"Por favor, ingresa una cadena de {long} cifras distintas.")
            continue

        aciertos = contar(numero_aleatorio, intento)
        print(f"Con {intento} has adivinado {aciertos} valores.")
        
        if aciertos == long:
            print("¡Felicidades! Has adivinado la cadena completa.")
            break

# Iniciar el juego
jugar()


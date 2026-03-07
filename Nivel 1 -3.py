import random
def num_aleatorio():
    num = random.randint(1, 100) 
    intento = int(input("Adivine el número de 1 a 100: "))
    if intento > num:
        print("El número es menor")
    elif intento < num:
        print("El número es mayor")
    else:
        print("¡Felicitaciones, adivinaste el número!")
num_aleatorio()

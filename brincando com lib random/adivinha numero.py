import random

numero = int(input("Digite um numero de 0 a 10"))
randomic = random.randint(0, 10)
if numero == randomic:
    print ("Parabens, você acertou, numero era:", numero)
else:
    print("Você errou!")
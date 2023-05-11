import random 


numero = int(input("Advinhe um numero de 0 a 10: "))

randomic = random.randint(0, 10)


while(numero != randomic):
    numero = int(input("Você errou! Tente novamente: "))
    
    if numero == randomic:
        print("Parabens, você acertou!!")
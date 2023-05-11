import random 


num1 = float(input("Digite o menor numero: \n\t"))
num2 = float(input("Digite o maior numero: \n\t"))

print(f'Agora será gerado um numero racional aleatorio no invervalo entre {num1:.0f} e {num2:.0f}:')

num_random = random.uniform(num1, num2)

print(f'{num_random:.2f}')
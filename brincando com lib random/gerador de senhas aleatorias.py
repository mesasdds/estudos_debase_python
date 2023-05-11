import random


print("Bem vindo ao gerador de senhas de 9 caracteres: ")
numeros = str(input("Se quiser apenas Numeros digite 'Y' ou 'N' para não ou 'Sair' para sair:  \n\t"))

while (numeros != 'Sair'):
    if (numeros == "Y" or 'y'):
        senha = random.randint(111111111, 999999999)
        print("Senha=", senha)
        break
    elif(numeros == "N" or 'n'):
        senhas_possiveis = 'abcdefghijklNmnopqrstuvwxyyz'
        secret = random.sample(senhas_possiveis, 6)
        palavra = ''.join(secret)
        complet = random.randint(100,999)
        complet_string = str(complet)
        print("Sua senha: ", palavra+complet_string)
        break
    else:
        print("Comando Incorreto!")
        
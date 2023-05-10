class Fila:
    def __init__(self, *args):   #<--- metodo init recebendo *args (podem ser postos infinitos argumentos)
        self.f = list(args) #<--- define a variavel que recebe os args que seram passados em formato de lista 
        
Fila(1,2,3).f  #<--- chamamos a classe Fila para passada de args e posteriormente .f para a chamada da lista



class Fila:
    def __init__(self, *args):  #ja explicado
        self.f = list(args)     #ja explicado
    def __repr__(self):           #<-- metodo especial para representação da lista de fato
        return f'Fila: {self.f}'    #<-- retorno de um texto string com a variavel da f que esta com args
    



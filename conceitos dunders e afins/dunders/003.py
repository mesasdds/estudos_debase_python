class Fila:
    def __init__(self, *args): #ja explicado
        self.f = list(args)    #ja explicado
    def __repr__(self):         #ja explicado
        return f'Fila: {self.f}'    #ja explicado
    def __setitem__(self, pos, val):    #<-- metodo especial que torna iteravel o objeto, ou seja, possivel de acrescentar/alterar valores
        self.f[pos] = val             #<-- com o [pos] teremos a posição e a possibilidade de set de um novo arg na posicao
    def __getitem__(self, pos):             #<-- metodo especial para retorno do iteravel 
        return self.f[pos]        #<-- retorno

fila = Fila(2,2,2,7)

fila[1] = 10


print(fila)
print(fila[2: ])
print(fila.f)
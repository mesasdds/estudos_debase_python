class Fila:
    def __init__(self, *args):              #ja explicado
        self.f = list(args)                         #ja explicado

    def __repr__(self):                         #ja explicado
        return f'Fila: {self.f}'              #ja explicado

    def __setitem__(self, pos, val):       #ja explicado
        self.f[pos] = val               #ja explicado
    
    def __getitem__(self, pos):             #ja explicado
        return self.f[pos]              #ja explicado

    def __lshift__(self, val):   #<-- esse metodo especial é permite atraves de um operador "<<" a definição de um append na nossa lista
        self.f.append(val)  #<-- definição da nossa lista recebendo o append desse novo valor val que sera acrescentado

    def __rshift__(self, val): #<-- esse metodo especial permite a inclusao do remove() que basicamente retirara um valor da nossa lista
        self.f.remove(val) if val < len(self.f) else ("batata")  #<-- a utilização do remove junto a um "if", o motivo é basico, ele precisa fazer o len(self.f) pois precisa saber se o valor esta no range da lista 
#<-- não podemos por exemplo em uma lista de 10 itens, pedir o remove do f[10] pois seria a 11 posição, que nao existiria e seria printado "batata"



fila = Fila(1,2,3,4,5,6,7,9,10)

print(fila)
print(fila[1])

fila[1] = 11
print(fila[1])
print(fila)


fila << 2 # <--- inserindo 2 na lista
print(fila)

fila >> 2 
print(fila)


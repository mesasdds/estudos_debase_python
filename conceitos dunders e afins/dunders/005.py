class Func:
    def __init__(self, val):      #<-- definição init com o argumento qualquer, nesse caso "val"
        self.val = val          #<-- valor da variavel val será setado na chamada da função init(ou seja, na chamada da classe)
    def __call__(self):         #<-- metodo especial que permite definição de Func como de fato uma função que retorna valores
        print(self.val)         #<-- retorno do valor self.val 


# não funciona - > Func(2)

f = Func(2)  # <-- uma classe se converteu em uma função, isso é incrivel// setamos o valor de val como 2 

f()       #<-- chamada da função
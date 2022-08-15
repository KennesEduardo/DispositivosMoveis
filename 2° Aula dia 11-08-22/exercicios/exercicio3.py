class Pessoa:
    def __init__(self,nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def n(self):
        print("Ola, meu nome é", self.nome)

    def i(self):
        print("minha idade é", self.idade)  

    def e(self):
        print("meu endereco é", self.endereco) 



p1 = Pessoa("Kennes", 12, 'bairro cidade jardim')
p1.n()
p1.i()
p1.e()

def altera():
    p1.e = ("Nadime derze n ddd420")

altera()   

print(p1.e)

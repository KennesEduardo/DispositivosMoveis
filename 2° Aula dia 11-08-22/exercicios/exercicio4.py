class Quadrado:
    def __init__(self,lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4

    def lados(self):
        print(self.lado1)
        print(self.lado2)
        print(self.lado3)
        print(self.lado4)


lista = []
for i in range(1,4+1):
    valor = input("informe lado do quadrado: ")
    lista.append(valor)        

print(lista)    

lado1 = lista[0]
lado2 = lista[1]
lado3 = lista[2]
lado4 = lista[3]

lados = Quadrado(lado1, lado2, lado3, lado4)

lados()
print(lados)




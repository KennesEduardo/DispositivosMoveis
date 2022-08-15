tamanho = int(input("Escreva a capacidade de sua lista: "))

lista = []
for i in range(1,tamanho+1):
    valor = input("digite qual quer valor")
    lista.append(valor)
  

print(lista)

def enumera():
    for i,valor in enumerate(lista):
        print(i,valor)

enumera()
import math as mt
# nome = input('Digite seu nome:')
#
# print("Seu nome é", nome)
# % pega o resto da divisap
# idade = 51
# peso = 2.75
# print(type(idade)) #

# print(round(peso))# round arredonda normal
# print(mt.ceil(peso))# ceil arredonda pra cima
# print(mt.trunc(peso))
# print(mt.floor(peso))
#
# print("bem vindo %.3f"%(peso))

# print('bem vindo', idade*mt.ceil(peso))
# print(dir(idade))
# idade = input('Digite sua idade:')

#comparação
# if idade <= 17:
#     print("voce e menor")
# elif idade >= 18 and 40:
#     print('voce e maior')
#
# else:
#     print('voce é idoso')

# if idade %2==0:
#     print("Par")
# else:
#     print('Impar')



#Listas
li = [1,2,'a','b', 2.4]
print(li[-2]) #pega o ultimo elemento
print(li[2:]) #pega da posição do para frenteo
print(li[2:4]) #pega da posição até a 4
li.append("cachorro") #adiciona ao final da Listas
li.insert(0,'altairrrrrr')
li.reverse()
print(li)


##tuplas
tu = (1,2,'ab',2.4)
print(tu)

# ##strings rever depois
# frase = 'Essa é minha frase'
# print(frase.islower())

##DICIONARIOS
dic ={1:"Altair", 2: 17, 3:"Rodrigo"}
print(dic.values()) #imprime todos
print(dic[1]) #seleciona 1 chave
dic[5]='teste' #adiciona ou altera uma chave
print(dic.values()) #imprime todos



##REPETIÇÃO
for i in range(0,len(li),2):
    print(li[i]) #imprimindo a lista pulando de 2 em 2

#enumerando a lista
for i,valor in enumerate(li):
    print(i,valor)


for i in range(0,10,1):
    print(i,valor)
print("")

##while
x = 4
while x<10:
    print(x)
    x+=1

#ARQUIVOS

file = open("teste.txt",'w')
file.writelines(['teste de gravação', '\nTeste de gravação 1'])
file.close()

file = open("teste.txt",'r')

for dados in file:
    print(dados)

file.close()

##ADICIONA OS DADOS DA LISTA NO ARQUIVO txt
file = open("teste.txt",'w')
file.write(str(li))
file.close()

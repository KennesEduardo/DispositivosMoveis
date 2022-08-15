lista = [1,2,4,5,10,11,12,14,15,20]


def dobro():
    soma = 0
    for i in range(0,len(lista)): 
        print(lista[i])
        soma += lista[i]
    print("Resultado da soma é igual a:",soma)    
    media = soma / 10
    print("A media do valor é", media)    

dobro()    



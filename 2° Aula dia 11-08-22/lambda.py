#-------Lambida-------
amp = lambda x,y,z:(x**2+y**2+z**2)**.5
print(amp(1,1,1))
print(amp(3,4,5))


#------MAPEAMENTO----

lista = [1,2,4,5,10,11,12,14,15,20]

#FUNÇÃO PARA DIVIDIR TODA A LISTA
new_lista = list(map(lambda x : x/2, lista))
print(list(map(lambda x: x**2, new_lista)))

#print(list(map(lambda x: x/2, lista)))

#FUNÇÃO PARA FILTRAR E PEGAR OS QUE SÃO PARES DA LISTA
print(list(filter(lambda x:not(x%2),lista)))

#lista comprehension
print([ x**2 for x in lista if not x%2])

#funão para imprimir todas as frutas que tenha letra M
frutas = ["maça", "banana", "pera", "uva", "melancia"]
print([ x for x in frutas if "m" in x])

#função para passar a lista toda para maiuscula 
print([x.upper() for x in frutas])

#função que muda os nome de todas as informação da lista para jaca
print([ x if x=="pera" else "jaca" for x in frutas])

print([[ j for j in range(3)] for i in range(3)])

print([ i*10 for i in range(1,50,2)])
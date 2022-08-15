for i in range(0,10,1):
    li = []
    li = input('Digite um número:')
    print(li)

    file = open("teste.txt",'a')
    file.writelines(li)
    file.close()





# li=[]
# x=0
# while x<10:
#     add=input
#     li.append(add)
#     x+=1
# print(li)

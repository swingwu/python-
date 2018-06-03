f1=open('C:/Users/wucaoyue/Desktop/1.txt','r')
f2=open('C:/Users/wucaoyue/Desktop/2.txt','r')
f3=open('C:/Users/wucaoyue/Desktop/3.txt','r')

r1=f1.read()
r2=f2.read()
r3=f3.read()

list1=r1.split()
list2=r2.split()
list3=r3.split()


list4=[]
for i in range(0,len(list1)):
    if list3[i] not in list1:
         pass
    elif list3[i] not in list2:
        pass
    else:
        list4.append(list3[i])
    print(list4)
    print(len(list4))


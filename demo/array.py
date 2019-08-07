import array
ar=array.array('d',[1,2,3,4,5])
for x in ar:
    print(x)
y=iter(ar)
print(next(y))
print(next(y))    

l=len(ar)
for z in range(0,l):
    print(ar[z])

from array import *
ar=array("i",[1,2,3,4,5])


for x in ar:
    print (x)     

list=[1,2,3,4,5]
list.reverse()
print(list) 
print (list[0])  




def reverse_recursion(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursion(s[1:]) + s[0]

str="Hello world"
print(reverse_recursion(str))



list=[[1,2,3,5],[5,6,7,8]]
print(list[1][2])
print(list[1][1])
for x in list:
    for y in x:
        print(y,end=" ")
    print()   



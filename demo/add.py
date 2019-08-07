x=input("enter 1 number")
y=input("Enter 2 number")
z=float(x)+float(y)
print (z)
n='hi'
m='hello'
print (n+m)

string=input("Enter string")
for x in range(0,(len(string))//2):
    if(string[x]!=string[len(string)-x-1]):
        print("no")
    else:
        print("yes")    

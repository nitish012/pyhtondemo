def fact(x):

    if(x==0 or x==1):
        return(x)

    else:
        return(x*fact(x-1)) 

x=int(input("enter a no"))
factorial=fact(x)
print("the factorial is {}".format(factorial))
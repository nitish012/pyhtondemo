
def prime(x):
 for i in range(2,x+1):
  if (x%i==0):
    break 
 if (i==x):
    print ("prime no")
 else:
    print ("not prime")

x=int(input("enter number "))
prime(x)

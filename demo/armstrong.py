def armstrong(x,y):
    for num in range(x,y):
        n=num
        sum=0
        while(n>0):
            rem=n%10
            sum=sum+int(rem**3)
            n=n/10
        if(sum==num):
            #print ("{} is armstrong".format(n))
            print("armstrong")
        else:
            print("not armstrong")      

x=int(input("enter first number "))
y=int(input("enter second number "))
armstrong(x,y)
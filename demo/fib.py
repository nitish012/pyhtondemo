def fibonacci(end):
    a,b=0,1


    while a<end:
        yield a
        a,b=b,a+b
#x=fibonacci(4)
for y in fibonacci(4):
    print (y)


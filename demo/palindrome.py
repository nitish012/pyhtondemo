def palindrome(n):
    num=n
    rev=0
    while(num!=0):
     rem=num%10
     rev=rev*10+rem
     num/=10

    if(rev==n):
       print("pallindrome")

    else:
       print("not pallindrome")

x=int(input("enter a no"))
palindrome(x)

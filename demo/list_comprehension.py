list=[1,2,3,4,5]
mylist=[n*2 for n in list if (n%2==0)]
print(mylist)

# def showlist(list):
#    output=["FizzBuzz" if (y%3==0 and y%5==0) else  "Fizz" if (y%3==0) else  "Buzz" if (y%5==0) else y for y in list]
#    print(output)

# lst=[]
# #strname=""
# num=int(input("enter a no of elements "))
# print("please enter the {} elements for list:".format(num))
# for x in range(0,num):
#     ele=int(input())
#     lst.append(ele)

# print(lst)     
# showlist(lst)    
   
#output=["Fizz" if (y==3) else  "Buzz" if (y==5) else  "fizzBuzz" if (y%3==0 and y%5==0) else y  for y in lst]
#mylst=["FizzBuzz" if (y%3==0 and (y%5==0)) else '' ("Fizz" if (y==3) or "Buzz" (y==5) for y in lst]
#print(output)
# mylst=["FizzBuzz" if(y%3==0)]


# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]

# common_num = [a  for a in list_a for b in list_b if a == b ]

# print(common_num)


# for y in lst:
#     if(y==3):
#         strname=strname+"fizz"
#         print(strname)
#     elif(y==5):
#         strname
#         strname=strname+"Buzz"
#         print(strname)
#     elif(y%3==0 and y%5==0):
#         strname=strname+"fixxBuzz"
#         print(strname)
            

#showlist(lst)
x = input("How many numbers in list?")
list_of_nums = [int(input("Enter number {}: ".format(n+1))) for n in range(int(x))]

for x in list_of_nums:
   if not(x%5 or x%3):
      print(x%5 or x%3)
      print("FizzBuzz")
   elif not(x%3):
      print(x%3)
      print("Fizz")
   elif not(x%5):
      print(x%5)
      print("Buzz")
   else:
      print(x)
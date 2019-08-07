class Student:
    def __init__(self,name,age,rollno):
        self.age=age
        self.name=name
        self.rollno=rollno

    def __gt__(self,other):
        return self.age>other.age

    def __eq__(self,other):
        return self.age==other.age

    def __lt__(self,other):
        return self.age<other.age    

print("Enter details of first student ")
name1=(input("Enter name "))
age1=int(input("Enter age "))
rollno1=int(input("Enter Rollno ")) 

obj1=Student(name1,age1,rollno1)

print("Enter details of second student ")
name2=(input("Enter name "))
age2=int(input("Enter age "))
rollno2=int(input("Enter Rollno "))

obj2=Student(name2,age2,rollno2)
#obj1=Student("akshay",15,12)
#obj2=Student("gaurav",18,10)
print("output :")
print("First student age is less than second student {}".format(obj1<obj2))
print("age is equal {}".format(obj1==obj2))
print("First student age is greater than second student {}".format(obj1>obj2))

import urllib
import http.client
class MyClass:
    x=10
print(MyClass().x)    

class Person:
  def __init__(this, name, age):
    this.name = name
    this.age = age

  def myfunc(self):
    print("Hello my name is " +self.name)
    print(self.age)

p1 = Person("John", 36)
p1.myfunc()


class student(Person):
    pass
#del p1.age
x=student("ashish",78)
print (x.age)
print (p1.age)


class demo:
  def __init__(self,age,color):
    self.age=age
    self.color=color

  def disp(self):
      print ("{} is my age".format(self.age))
      print("shirt is {}".format(self.color))

x=demo(23,"red")
x.disp()

class test(demo):
  pass

y=test("24","white")      
y.disp()

class example(test):
  def __init__(self,age,name):
   test.__init__(self,age,name) 
   self.age=age
   self.name=name
  def show(self):
    print (self.age)
    print (self.name)

example(21,"nitish").show()
example(21,"nitish").disp()

class A(object):
    def fun(self):   
     pass
ins_a = A.fun
ins_b = A().fun
print(ins_a)
print(ins_b)



    


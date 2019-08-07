tupple=("nitish","mayank","vaibhav")
mytupple=iter(tupple)
print (next(mytupple))
print (next(mytupple))
print (tupple)

mystring=tupple[1]
st=iter(mystring)

print(next(st))
print(next(st))
print(next(st))

class student:
    def __iter__(self):
        self.a=3
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
y=student()
z=iter(y)

print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))


import random
print(random.randint(2,10))
#print(random.choice(1))

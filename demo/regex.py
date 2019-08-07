import re
text="The Animal mammal"
x=re.search("the.*Animal$",text)
print(x)
if(x):
    print("yes")

else:
    print("no")

y=re.findall("mal",text)
print(y)
z=re.findall("nice",text)
print(z)
p=re.search("ma",text)
print(p.span)    
print(p.start())
#s=re.split("\s",text,1))

# Python code to demonstrate dictionary 
# comprehension 

# # Lists to represent keys and values 
# keys = ['a','b','c','d','e'] 
# values = [1,2,3,4,5] 

# # but this line shows dict comprehension here 
# myDict = { k:v for (k,v) in zip(keys, values)} 

# # We can use below too 
# # myDict = dict(zip(keys, values)) 

# #print (myDict) 

d=[1,2,3,4,5]
e={"a","b","c"}
# di={1,2,3,4}
myDict={e:d for (e,d) in zip(e,d)}
mydict=zip(d,e)
#mydict=set(zip(d,e))
print(myDict) 
#d,e=zip(*myDict)
d,e=zip(*mydict)
print(d)
print(e)

thislist1=['color','car']
thislist2=['red','bmw']

thisdict={key:value for (key,value) in zip(thislist1,thislist2)}
print(thisdict)

mapped=list(zip(thislist1,thislist2))
print(mapped)
val1,val2=zip(*mapped)
print(list(val1),list(val2))




thissetlist=[1,2,3,4,5]
thisset=set()
for x in thissetlist:
    if(x%2):
        thisset.add(x)

print(thisset)
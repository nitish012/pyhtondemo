import pandas as pd
data=['a','b','c']
a=pd.Series(data)
print(a)
index=["1","2","3"]
b=pd.Series(data,index)
print(b)
dic={'a':1,"b":2,"c":3}
c=pd.Series(dic,index)
print(c)
data1=[[1,2,3],[4,5,6]]
d=pd.Series(data1)
print(d)

# DataFrame
data2={'a':1,"b":2}
data3={'c':3,"d":4}
datas={'first':data2,'second':data3}
e=pd.DataFrame(datas)
print(e)

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')    
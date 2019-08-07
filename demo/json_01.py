import json

x='{"car":"bmw","color":"red"}'
y=json.loads(x)
print (y["car"]) 



# import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
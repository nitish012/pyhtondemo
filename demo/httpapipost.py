# import requests
# import json
# payload={'a':1,"c":2,"b":3}
# resp=requests.post("https://httpbin.org/post",data=payload)
# data=resp.json()
# print(resp.text)
# print(data)
# print(type(data))


# import json
# person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'
# person_dict = json.loads(person_string)
# print(person_dict)
# #print(json.dumps(person_dict, indent = 4, sort_keys=True))
# print(json.dumps(person_dict,sort_keys=True))

# with open('person.txt', 'w') as json_file:
#   json.dump(person_dict, json_file)

# json parsing

data={"vehicle":"car","name":{"firstname":"pankaj","lastname":["a","b"]},"detail":["book","student"]}
for x in data:
  # print(x.get("vehicle"))
  # print(x.get("name"))
  print(x)
  print(data[x])
print(data["vehicle"])
namedict=data.get("name")
print(namedict.get("lastname"))
detaillist=data.get("detail")
print(detaillist[0])
length=len(namedict["lastname"])
for x in range(length):
  print(namedict.get("lastname")[x])



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
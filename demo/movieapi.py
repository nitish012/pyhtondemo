import requests
import json
import csv
import os

def fetchingTitle(movie):
    resp1=requests.get("http://www.omdbapi.com/?t={}&apikey=7ca730a6".format(movie))
    return resp1

def fetchingId(id):
    resp2=requests.get("http://www.omdbapi.com/?i={}&apikey=7ca730a6".format(id))   
    return resp2 
#resp2=requests.post("http://www.omdbapi.com/?i=tt3896198&apikey=7ca730a6")
#data1=resp1.json()
#data2=resp2.json()
# print(type(data2))
# print(json.dumps(data2,indent=4))

# print(data2.get("DVD"))
# print(data2["imdbID"])
# print(data2["Actors"])
# print("\n")
# print("--------------------")
x=int(input("how many shows want to see" ))
lst=[]
for shows in range(x):
    movie=(input("Enter movie name "))
    resp1=fetchingTitle(movie)
    response1=resp1.json()
    print(json.dumps(response1,indent=4))
    print(" ------------------ ")
    id=response1['imdbID']
    resp2=fetchingId(id)
    response2=resp2.json()
    print(response2)
    print(json.dumps(response2,indent=4))
    print(response2['Actors'])
    #print(response2.values())
    lst.append(response2["Ratings"][0]['Value'])
#print(respond.json())
print(lst)
new_list=lst.sort()
print(new_list)
print('max Rating is: %s:'% (max(lst)))



# f=open("first.csv","w")
# ''' create csv file'''
# csvwriter=csv.writer(f)
# #csvwriter.writerow(["Rated","Response","country"])
# csvwriter.writerow(data2.keys())
# csvwriter.writerow(data2.values())
# #for x in data2:
#     #csvwriter.writerow([data2["Rated"],data2["Response"],data1["Country"]])
#     #csvwriter.writerow(data2[x])
# f.close()

# with open('first.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))


# '''  Reading a csv file'''
# with open('first.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# with open('first.csv', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# print(data2["Country"])
# print(data2["Ratings"][0]['Source'])
# for y in data2["Ratings"][0]:
#     print(data2["Ratings"][0]['Source'])

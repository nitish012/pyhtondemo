import json
import requests

payload={'a':1,'b':2}
def posts():
   resp=requests.get("https://jsonplaceholder.typicode.com/posts",params=payload)
   return resp

def no_of_posts(user_id):
   post=requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={str(user_id)}")
   return post

def no_of_comments(post_id):
   comments=requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={str(post_id)}")
   return comments

def post_id_comments():
   post_id=requests.get("https://jsonplaceholder.typicode.com/comments")
   return post_id                   

response=posts()
data=response.json()
length=len(data)

# Display user with no posts and no of comments
for i in range(length):
   response_posts=no_of_posts(i+1)
   posts_data=response_posts.json()
   len_postdata=len(posts_data)           #getting total no of post
   
   print("userid:{}".format(i+1))
   print("No of Post:{}".format(len_postdata))
   print("No of Comments:{}".format(len_postdata))
   for titl in posts_data:
      Title=titl.get('title')
      print("Title:{}".format(Title))
   print(" ")   
print(" ")   
  
# Display user with no of post and most commented post
for i in range(length):
   response_comments=no_of_comments(i+1)
   response_most_comments=post_id_comments()
   comments_data=response_comments.json()
   mostcommented_data=response_most_comments.json()
   countspost=0
     # finding no of post of user         
   for id in mostcommented_data:
      
      Id=id.get('postId')   
      if(Id==i):
         countspost+=1             
   len_commentsdata=len(comments_data)   
   
   print("user:{}".format(i+1))
   print("post:{}".format(countspost))
   print("most commented post:{}".format(len_commentsdata))
    #fetching email of user    
   for em in comments_data:
      Email=em.get('email')
      print("Email:{}".format(Email))
   print(" ")   
print(" ") 


#Display user post with no of comments
for i in range(length):
   respond_comments=no_of_comments(i+1)
   comment_data=respond_comments.json()
   no_comments=len(comment_data)
   print("post:{}".format(i+1))
   print("No of Comments {}".format(no_comments))




# for x in data1:
#    countcomments=0
#    t = PrettyTable(['UserId','No of Posts','Title','No of Comments'])
#    t.add_row([x['postId'],x['id'],x['name'],x['id']])
#    print(t)



# new=json.loads(data2)
# newdata=json.dumps(data2,sort_keys=True)
# print(newdata)
# newdata=json.dumps(x,sort_keys=True)
# t = PrettyTable(['UserId','No of Posts','Most Commented post'])
# for x in data2:
#    t.add_row([x['postId'],x['id'],x['body']])
#    #print(t)
# print (t.get_string(sortby="No of Posts",reversesort=True))

   

  




   
   #print("_____________")
   #print((x[0].values()['id']))
   #print(x.values()['id'])
   # print(x[0]['id'].values())
   #print(data[x])


'''
for getting whole fields of Table
'''
# for x in data:
#    t = PrettyTable(['title', 'id', 'userId', 'body'])
#    t.add_row(x.values())
#    print((dat[0]['id']))
#    print (t)   
    
    #data['A']['B']['unknown']['maindata'][0]['Info']
# for x in dat:
#    t = PrettyTable(['id', 'userId'])
#    t.add_row(dat['x']['id'])
#    t.add_row(dat['x']['userId'])
#    print(t)
#print(data[1]['id'])


      
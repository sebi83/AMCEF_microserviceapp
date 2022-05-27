import json
import requests

#user ID and post json data
URL = 'https://jsonplaceholder.typicode.com/posts/'
post_data = requests.get(URL, headers={'Content-Type':
                                       'application/json'}).json()

userid_data = requests.get(URL, headers={'Content-Type':
                               'application/json'}).json()



#title and body get

post_data = requests.get(URL, headers={'Content-Type':
                                 'application/json'}).json()


print (post_data[2])










#  {
#     'userID': fetched['userID'],
#     'id': fetched['id'],
#     'title': fetched['title'],
#     'body': fetched['body'],
# })

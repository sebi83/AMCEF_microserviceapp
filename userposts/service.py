import json
import requests


URL = 'https://jsonplaceholder.typicode.com/posts/'

data = requests.get(URL, headers={'Content-Type':
                               'application/json'})
response = json.dumps(data)
print(response)



#  {
#     'userID': fetched['userID'],
#     'id': fetched['id'],
#     'title': fetched['title'],
#     'body': fetched['body'],
# })

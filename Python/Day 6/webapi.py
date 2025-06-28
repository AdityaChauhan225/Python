#### WEB API
'''
api is a set of rules that allows one software application to interact with another 
a web api is accessed over the internet using http requests and response and the data is returned in json format
'''
## methods
'''
GET : fetch data
POST : post data
PUT : post data 
DELETE
'''

### json 
'''
stands for javascrit object notaion
it is a light weight data format used to exchange data between web clients and servers. 
very simmilar to python dictionary 
'''
import json as j
import requests as rq

# data={
#     'name':'Alice',
#     'age':25
# }
# json_str = j.dumps(data) ### converts to json
# print(json_str)

# json_data = "{'name':'Alice','age':25}"

# data= j.loads(json_data)
# print(data["name"])

#


# x={
#     "name":"json",
#     "age":3,
#     "married":True,
#     "divorced":False,
#     "children":("ann","billy"),
#     "pets":None,
#     "cars":[
#         {"model":"BMW 230","mpg":27.5},
#         {"model":"Ford egde","mpg":24.1}
#     ]
# }

# print(j.dumps(x))
# print(x["cars"][1]["model"])

url='https://en.wikipedia.org/wiki/Machine_learning'
x= rq.get(url)
print(x.content)

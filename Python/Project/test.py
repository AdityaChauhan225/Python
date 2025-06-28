import requests as rq

ipurl="http://ip-api.com/json"

ip = rq.get(ipurl)
ipad=ip.json()

print(ipad)
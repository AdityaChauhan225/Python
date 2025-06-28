import requests as rq

# api key a11ad1523105459893e184514252706

ipurl="http://ip-api.com/json"

ip = rq.get(ipurl)
ipad=ip.json()


if ipad['status']=='success':
    lat=ipad['lat']
    long=ipad['lon']


    Url = f"http://api.weatherapi.com/v1/current.json?key=a11ad1523105459893e184514252706&q={lat},{long}"
    weather=rq.get(Url)
    data= weather.json()
    print(f"Wether out side: {data['current']['condition']['text']}")
    print(f"Temperature: {data['current']['temp_c']}c")
    print(f"What is feels like: {data['current']['feelslike_c']}c")
    print(f"Speed of wind : {data['current']['wind_kph']}kmph")
    print(f"level of humidity: {data['current']['humidity']}%")
    print(f"How much is it cloudy today: {data['current']['cloud']}%")

    if data['current']['is_day'] == 1:
        print(f"Is it day: Yes")
    else:
        print("Is it day: No it's night")


    print(f"Uv index: {data['current']['uv']}")
    print(f"Location: {data['location']['name']},{data['location']['region']} ,{data['location']['country']}")
    # print(f"{data['location']['region']}")
    # print(f"{data['location']['country']}")
    print(f"Time: {data['location']['localtime']}")

else:
    print("Not able to fetch location automatically.")






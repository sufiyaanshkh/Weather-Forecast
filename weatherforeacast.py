import requests

city = input("Enter the city name")
print(city)

print("Displaying weather report:"+city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

print(res.text)

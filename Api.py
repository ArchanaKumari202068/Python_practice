import http.client

conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "4d4681c3c1msh99bc636ee9c2e93p1a2dc7jsnd2c7cb878680",
    'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

conn.request("GET", "/forecast/3hourly?lat=35.5&lon=-78.5", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
# https://rapidapi.com/weatherapi/api/weatherapi-com/
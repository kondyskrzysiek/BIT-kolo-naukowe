import requests

class Weather:
    def __str__(self,json):
        return f'city: {json["name"]} , description: {json["weather"][0]["description"]} , temp: {float(json["main"]["temp"])} , pressure: {float(json["main"]["pressure"])}' \
               f' , humidity: {float(json["main"]["humidity"])} , air speed: {float(json["wind"]["speed"])}'


class OpenWeatherApiClient:
    def __init__(self,api_key):
        self.api_key = api_key
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self,city: str):
        params = {'q':city,
                  'appid':self.api_key,
                  'units':'metric'}

        result = requests.get(self.base_url,params)

        return Weather.__str__(self,result.json())

if __name__ == '__main__':
    api_key = input('api key: ')

    citis = ['London','Warsaw','new york']

    api_client = OpenWeatherApiClient(api_key)
    weathers = [api_client.get_weather(city) for city in citis]

    for weather in weathers:
        print(weather)
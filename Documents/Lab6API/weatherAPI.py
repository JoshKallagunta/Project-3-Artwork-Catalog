import requests
import os

def main():
    key = os.environ.get('WEATHER_KEY')

    city_code = str(input('Enter what city you would like to check the weather: '))
    country_code = str(input('Enter the 2 Digit country code: '))
    query = {'q': (city_code, country_code), 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/weather'

    data = requests.get(url, params=query).json()
    weather_description = data['weather'] [0] ['description']
    temp = data['main'] ['temp']

    #I chose not to add the date and time into this program, tried using 'dt', however the formatting is not right
    #and for some reason 'dt_txt is giving me a Tracbeack error 
    #date_time = data['dt_txt']

    print(f'The weather is {weather_description}, the temp is{temp: .2f}F. ')
    #print(f'The time and date is {date_time}')

if __name__ == '__main__':
    main()


import requests

#data = requests.get('https://catfact.ninja/fact').json()
#print(data)
#fact = data['fact']
#print(f'A random cat fact is: {fact}')

#another_data = requests.get('https://api.kanye.rest').json()
#print(another_data)
#quote = another_data['quote']
#print(f'A random Kanye quote is: {quote}')

coin_data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
print(coin_data)

get_usd = float(input('Enter the amount of money you want to calculate, in USD' ))

USD = coin_data['USD']
print(f'The price of bitcoin is {USD} ')



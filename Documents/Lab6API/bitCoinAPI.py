import requests

def main():
    #User input of how many bitcoin they have
    number_of_bitcoin = float(input('How much bitcoin do you have? '))

    #URL request
    bitcoin_price_url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    #Getting the rate price from the API using permaters
    bitcoin_rate = bitcoin_price_url['bpi'] ['USD'] ['rate_float']

    #Calculating the current price of bitcoin, based on the user amout 
    USD_Calculation = bitcoin_rate * number_of_bitcoin

    #Printing how much the user's bitcoin is worth
    print('You have ${:.2f}'.format(USD_Calculation) + ' worth of bitcoin!')

if __name__ == '__main__':
    main()


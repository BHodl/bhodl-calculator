import json, requests, datetime, sys

def get_headers():
    """Get autorisation headers"""
    headers = {}
    headers["accept"] = "application/json"
    #headers["Authorization"] = "Bearer {}".format('logic')
    return headers

# Handle requests
def get_data(endpoint):
    """Get data request"""
    headers = get_headers()
    if headers and endpoint:
        response = requests.get(endpoint, headers=headers, verify=True)
        return json.loads(json.dumps(response.json()))
    else:
        return None

def get_hodl(data):
    # data = [currency, date, amount]
    currency = data[0]
    date = data[1]
    amount = int(data[2])
    date = "{}-{}-{}".format(date.day, date.month, date.year)
    endpoint = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date={}&localization=False".format(date)
    response = get_data(endpoint)
    buy_price = response['market_data']['current_price'][currency]
    btc_amount = amount / buy_price
    date_now = datetime.date.today()
    d = date_now
    date = "{}-{}-{}".format(d.day, d.month, d.year)
    endpoint = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date={}&localization=False".format(date)
    response = get_data(endpoint)
    now_price = response['market_data']['current_price'][currency]
    now_value = int(btc_amount * now_price)
    gain_lost = ''
    if buy_price <= now_price:
        gain_lost = 'gain'
    else:
        gain_lost = 'loss'
    percent = int(((now_price - buy_price) / buy_price) * 100)
    return { 'now_value': now_value, 'gain_lost': gain_lost, 'percent': percent }

if __name__=='__main__':
    print(sys.argv[1:])
    get_hodl(sys.argv[1:])
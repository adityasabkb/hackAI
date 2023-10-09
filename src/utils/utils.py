import os
import requests

#function to convert user input
def convert(secondary, threshold):
    s = secondary.split()
    t = threshold.split()
    t = [float(i) for i in t]
    d = dict(zip(s, t))
    return s, d

API_KEY = os.environ.get("CURRENCY_EXCHANGE_API")
print(API_KEY)
BASE_URL = "https://api.apilayer.com/currency_data/live?" #source=USD&currencies=JPY,INR"

payload = {}
headers= {
  "apikey": API_KEY
}

#function to get exchange rate of currencies 
def get_rate(secondary_currencies,base_currency="EUR"):
    url = BASE_URL
    url+=f"source={base_currency}&currencies="
    for i in secondary_currencies:
        url+=i + ","
    url = url[:-1]
    response = requests.request("GET", url, headers=headers, data = payload)

    status_code = response.status_code
    assert status_code==200

    result = response.json()
    final_dict = {}
    for i in secondary_currencies:
        final_dict[i] = result["quotes"][base_currency+i]
    return final_dict
    
if __name__=="__main__":
    print(get_rate(["INR","AED"],"EUR"))
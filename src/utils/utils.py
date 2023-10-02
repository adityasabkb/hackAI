import os
import requests

EXCHANGE_RATE_API = os.environ.get("EXCHANGE_RATE_API")

BASE_LINK = f"http://api.exchangeratesapi.io/v1/latest?access_key={EXCHANGE_RATE_API}"

#function to convert user input
def convert(secondary, threshold):
    s = secondary.split()
    t = threshold.split()
    t = [float(i) for i in t]
    d = dict(zip(s, t))
    return s, d

#function to get exchange rate of currencies 
def get_rate(secondary_currencies,base_currency="EUR"):
    if type(secondary_currencies) in (list,tuple):
        currencies = ""
        for i in secondary_currencies:
            currencies+=i+","
        if base_currency!="EUR":
            currencies+=base_currency+","
        
        FINAL_LINK = f"{BASE_LINK}&symbols={currencies}&format=1"
    else:
        currencies = secondary_currencies
        
        if base_currency!="EUR":
            currencies+=base_currency+","
        
        FINAL_LINK = f"{BASE_LINK}&symbols={currencies}&format=1"

    #----------FINAL_LINK CREATED---------------
    # print(FINAL_LINK)

    response = requests.get(FINAL_LINK)

    if response.status_code!=200:
        print("error")
        return -1
    else:
        data = response.json()
        # print(data)
        # print(data["rates"],type(data["rates"]))
    #-----------GETTING RESPONSE FROM FINAL LINK----------
    data["rates"]["EUR"] = 1
    final_dict = {}
    if type(secondary_currencies) in (list,tuple):
        for i in secondary_currencies:
            final_dict[i]= data["rates"][i]/data["rates"][base_currency]
    else:
        final_dict[secondary_currencies] = data["rates"][secondary_currencies]/data["rates"]
    return final_dict
if __name__=="__main__":
    print(get_rate(["INR","AED"],"EUR"))
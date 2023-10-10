# CurrencyExchangeAgent
HackAI IITB Techfest

This is an AI agent that utilizes Fetch.ai’s uAgents library to:
 1. Allows users to select their base currency and one or more foreign currencies they wish to monitor.
 2. Connects to a currency exchange API to fetch real-time exchange rates.
 3. Lets users set thresholds for alerts (e.g., notify me if 1 USD becomes more than 82.60 INR or less
than 82.55 EUR).
 4. Sends an alert/notification to the user when the exchange rate crosses the thresholds they've set.



## Prerequisites (optional):
Poetry is used to create a virtual enviornment so other python
 processes do not interfere with the uagents functions
```
pip install poetry
```




## Installation:

1. Clone the git repository to your computer
```
git clone https://github.com/adityasabkb/hackAI.git
cd hackAI
```


2. Create Virtual Enviornment (optional)
```
poetry init -n && poetry shell
```



3. Install Requirements
```
pip install -r requirements.txt
```

4. Adding API key to path variable
   1. Sign-in on [APILayer](https://apilayer.com/) to get your API key.
   2. Add CURRENCY_EXCHANGE_API=< your api key > to a .env file inside the src folder.


## Run:
```
cd src
python main.py
```


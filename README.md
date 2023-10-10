# CurrencyExchangeAgent
HackAI IITB Techfest

This is an AI agent that uses uagents library to:
1. Fetch real-time exchange rates of the currencies
2. Let users set a minimum and a maximum threshold value for each currency



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


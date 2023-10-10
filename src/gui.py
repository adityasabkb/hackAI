import ttkbootstrap as ttk
from ttkbootstrap.constants import *


root = ttk.Window(themename="darkly")
root.title("Currency Exchange")
root.geometry("700x500")

test = ttk.Label(root, text="Test")
test.grid(row = 0, column = 4, pady = 2)

currency_list = ["AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN", "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOV", "BRL", "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHE", "CHF", "CHW", "CLF", "CLP", "COP", "COU", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HTG", "HUF", "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MXV", "MYR", "MZN", "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "CNY", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLE", "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS", "UAH", "UGX", "USD", "USN", "UYI", "UYU", "UYW", "UZS", "VED", "VES", "VND", "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD", "XDR", "XOF", "XPD", "XPF", "XPT", "XSU", "XTS", "XUA", "XXX", "YER", "ZAR", "ZMW", "ZWL"]
secondary_currency = []
base_currency = ""
thresholdmin = []
thresholdmax = []

def validate_currency(x) -> bool:
    if x in currency_list:
        return True
    else:
        return False

currency_func = root.register(validate_currency)


#Base Currency Block
base = ttk.Label(root, text="Base Currency")
base.grid(row = 0, column = 0, sticky = W, pady = 2)

base_menu = ttk.Combobox(root,  values=currency_list, validate="key", validatecommand=(currency_func, '%P'))
base_menu.grid(row = 1, column = 0, pady = 2)
base_menu.current(0)




#Secondary currency block
secondary = ttk.Label(root, text="Secondary Currency")
secondary.grid(row = 0, column = 1, sticky = W, pady = 2)

secondary_menu = ttk.Combobox(root,  values=currency_list, validate="key", validatecommand=(currency_func, '%P'))
secondary_menu.grid(row = 1, column = 1, pady = 2)
secondary_menu.current(0)



#Add Button
def add_currency():
    secondary_currency.append(secondary_menu.get())
    test.config(text=f"{secondary_currency} and {base_menu.get()}")
    

add_button = ttk.Button(root, text="Add", command=add_currency)
add_button.grid(row = 3, column = 1, pady = 100)



#calculate Button
def calculate():
    global base_currency
    base_currency =  base_menu.get()
    test.config(text=f"{secondary_currency} and {base_currency}")

    
add_button = ttk.Button(root, text="Calculate", command=calculate)
add_button.grid(row = 4, column = 1, pady = 100)



root.mainloop()

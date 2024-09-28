
conversion_rates = {
    'INR': {'USD': 0.012, 'KRW': 15.812, 'JPY': 1.729},
    'USD': {'INR': 83.621, 'KRW': 1322.220, 'JPY': 14.581},
    'KRW': {'USD': 0.001, 'INR': 0.063, 'JPY': 0.109},
    'JPY': {'USD': 0.007, 'INR': 0.578, 'KRW': 9.145}
}

def convert_currency(amount, from_currency, to_currency):
  
    try:
        
        rate = conversion_rates[from_currency][to_currency]
        converted_amount = amount * rate
        return round(converted_amount, 2)  
    except KeyError:
       
        print(f"Conversion from {from_currency} to {to_currency} is not available.")
        return None

def currency_converter():
 
    print("Welcome to the Currency Converter!")
    while True:
      
        amount = float(input("Enter the amount you want to convert: "))
        from_currency = input("Enter the source currency (INR, USD, KRW, JPY): ").upper().strip()
        to_currency = input("Enter the target currency (INR, USD, KRW, JPY): ").upper().strip()

      
        result = convert_currency(amount, from_currency, to_currency)

        if result is not None:
            print(f"{amount} {from_currency} is = to {result} {to_currency}.")
        
      
        cont = input("Do you want to convert another amount? (yes/no): ").lower()
        if cont != 'yes':
            print("THANK YOU!")
            break

if __name__ == "__main__":
    currency_converter()

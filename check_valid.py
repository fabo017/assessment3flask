def validity(list, currency1, currency2, amount):
    result = []

    if currency1 not in list:
        result.append(f"{currency1} is not a currency") 
    if currency2 not in list:
        result.append(f"{currency2} is not a currency")

    try:
          if int(amount) <= 0:
            result.append(f'Amount should be a positive number, your amount is {amount}') 
    except ValueError:
        result.append(f"{amount} is not a number") 
  
    return result
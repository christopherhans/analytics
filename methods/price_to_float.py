def price_to_float(price):
    price = float(price.replace('$','').replace(',',''))
    # price = price * 0,9
    return price

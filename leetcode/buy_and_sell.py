price = [5,6,7]

buy_price = min(price)
for i in range(price):
    if price[i]==buy_price:
        day = i
profit = buy_price - price[day+1]

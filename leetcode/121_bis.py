prices =  [7,1,5,3,6,4,24,72,82,1,363]

left = 0 
right = 1

max_profit = 0 

while right < len(prices):
    current_price = prices[right] - prices[left]
    if prices[left]<prices[right]:
        max_profit = max(current_price, max_profit)
    else :
        left = right
    right +=  1
print(max_profit)
prices = [7,1,5,3,6,4]

left=0  #Buy --> Pointer --> I'm buying the stock
right=1 #Sell --> Pointer --> I'm selling it 

max_profit = 0 # The variable that contains the maximal profit

while right < len(prices): # Going through the array in one time 
    current_profit = prices[right] - prices[left] # The current profit -> The profit when i'm just going through the array
    if prices[left]<prices[right]:  #The best condition for me 
        max_profit = max(current_profit, max_profit)
    else: 
        left = right # I'm changing the position -> I'm looking for the next day to buy 
    right+=1
print(max_profit)




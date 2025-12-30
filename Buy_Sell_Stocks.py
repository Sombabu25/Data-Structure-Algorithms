prices = [7,1,5,3,6,4]
buy = prices[0]
sell = 0
profit = 0

for i in range(1, len(prices)):
    if prices[i] < buy:
       buy = prices[i]
    
    curr_profit = prices[i] - buy

    if curr_profit > profit:
       profit = curr_profit
       sell = prices[i]   

      #  profit = sell - buy

      #  sell = prices[i+1]

      #  curr_profit = sell - buy

      #  if curr_profit > profit:
      #     profit = curr_profit
print(profit)



# best-time-to-buy-and-sell-stock-leet-code
prices = [7,1,5,3,6,4]
max_profit = 0
min_price = float('inf')
for price in prices:
    if price < min_price:
        min_price = price
    else :
        max_profit = max(max_profit, price-min_price)
print(max_profit)

# Time Complexity O(n)
# Space Complexity O(1)


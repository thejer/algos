def buy_sell_stock(stock_prices):
    length = len(stock_prices)
    profit = 0
    if length == 1:
        return profit
    buy = stock_prices[0]
    for i in stock_prices:
        if i < buy:
            buy = i
        else:
            profit = max(profit, i - buy)
    return profit


print(buy_sell_stock([7, 6, 4, 3, 1]))

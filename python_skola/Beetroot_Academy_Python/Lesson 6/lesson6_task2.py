def calculate_stock(in_stock, in_prices):
    total_stock = 0

    for item in in_stock:
        item_total = in_stock[item] * in_prices.get(item, 0)
        total_stock += item_total

    return total_stock


stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

# def total_value():
#     for key in stock:
#         if key in prices:
#             x = stock.get(key)  # value of keys in stock
#             y = prices.get(key)  # value of keys in prices
#             print(key, "total price is:", x * y)
#
#
# total_value()





print("total price in stock:", calculate_stock(stock, prices))
stock["lemon"] = 2
prices["lemon"] = 2.5
print("total price in stock:", calculate_stock(stock, prices))

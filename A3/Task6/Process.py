def process_prices(prices):
    discounted_prices = list(map(lambda price: price - price * 0.1, prices))
    filtered_prices = list(filter(lambda price: price > 300, discounted_prices))
    return discounted_prices, filtered_prices

print(process_prices([100, 500, 900, 50, 750]))
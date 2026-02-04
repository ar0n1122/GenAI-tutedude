prices = [100, 250, 400, 1200, 50, 2000, 850]

prices_greater = list(filter(lambda price: price > 500, prices))
prices_smaller = list(filter(lambda price: price <= 500, prices))


print("Original Prices:", prices)
print("Prices Greater than 500:", prices_greater)
print("Prices Smaller than or Equal to 500:", prices_smaller)
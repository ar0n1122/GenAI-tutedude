## Task 1
products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch", "Camera"]

sample_product = ("Smartphone", 699.99, "Electronics") # tuple

print(products[1])  # 2nd item
print(products[-1])  # last item

# new products
products.append("Smart Speaker")
products.append("Bicycle")

# optional
sample_product = [599 if i == 1 else x for i, x in enumerate(sample_product)]  # convert tuple to list
sample_product = tuple(sample_product)  # convert back to tuple


## Task 2
categories = ["Electronics", "Electronics", "Electronics", "Audio", "Utility", "Utility", "Audio", "Sports"]
categories_set = set(categories)  # unique categories

print(categories_set)
categories_set.add("Audio")  # add a duplicate
print(categories_set)

audio_exits = "Audio" in categories_set  # check existence
print(audio_exits)

print(len(categories_set))  # number of unique categories


## Task 3
price_dict = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Tablet": 399.99,   
    "Headphones": 199.99,
    "Smartwatch": 299.99,
    "Camera": 499.99
}

price_dict["Smart Speaker"] = 149.99  # add new product
price_dict["Smartphone"] = 10.99  # updated exisitng

if "Tablet" in price_dict:
    del price_dict["Tablet"]  # remove product and handled safely

sum = 0
for i in price_dict.values():
    sum += i  # sum price of all products

avg = sum / len(price_dict)  # average price
print(f"Average price: {avg}")

# optionals
most_expensive_product = max(price_dict, key=price_dict.get)  # product with highest price
print(f"Most expensive product: {most_expensive_product} - ${price_dict[most_expensive_product]}")

least_expensive_product = min(price_dict, key=price_dict.get)  # product with lowest price
print(f"Least expensive product: {least_expensive_product} - ${price_dict[least_expensive_product]}")


## Task 4
catalog = [(product, price_dict[product], categories[idx]) for idx, product in enumerate(products) if product in price_dict.keys()]  # list of tuples (product, price, category)
print(catalog)

category_to_products = {}
for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []
    category_to_products[category].append(product)  # group products by category

print(category_to_products)
x =  max(category_to_products, key=lambda k: len(category_to_products[k]))  # category with most products
print(category_to_products.get(x))
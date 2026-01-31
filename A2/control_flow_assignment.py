# Task 1
order_amount = 0
try:
    order_amount = int(input("Enter the order amount: "))
except ValueError:
    print("Invalid input. Please enter a numeric value.")
    exit()
discount=0
if order_amount >= 2000:
    discount = 0.15
elif order_amount >= 1500 and order_amount < 2000:
    discount = 0.10
elif order_amount >= 1000 and order_amount < 1500:
    discount = 0.07

# optional 
order_discount = order_amount * discount
discounted_amount = order_amount - order_discount
taxed_amount = discounted_amount * 0.05 # 5% tax on discounted amount
final_amount = discounted_amount + taxed_amount

## Task 2
def discount_rate(order_amount):
    if order_amount >= 2000:
        return 0.15
    elif order_amount >= 1500:
        return 0.10
    elif order_amount >= 1000:
        return 0.07
    else:
        return 0.0
    
orders = [1200, 2500, 800, 1750, 3000]
res = []
for amount in orders:
    rate = discount_rate(amount)
    res.append((amount, rate, amount - amount * rate))

total_revenue = 0
for result in res:
    print(f"Order Amount: {result[0]}, Discount Rate: {result[1]*100}%, Final Amount: {result[2]}")
    total_revenue += result[2]
print(f"Total Revenue: {total_revenue}")

# optional
print(len([result for result in res if result[1] > 0]))  # number of orders with discount


# Task 3
input_value = input("Enter 1 to add an order amount, 2 to view all orders, q to quit: ")
amount=0
orders = []
while input_value != 'q':
    if input_value == '1':
        try:
            amount = int(input("Enter the order amount to add: "))
            orders.append(amount)
            print(f"Order amount {amount} added.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    elif input_value == '2':
        print("Current Orders:")
        for order in orders:
            discount=0
            if order_amount >= 2000:
                discount = 0.15
            elif order_amount >= 1500 and order_amount < 2000:
                discount = 0.10
            elif order_amount >= 1000 and order_amount < 1500:
                discount = 0.07 
            print(f"Order Amount: {order}, Discount Rate: {discount*100}%, Final Amount: {order - order * discount}")
    else:
        print("Invalid option. Please try again.")
    input_value = input("Enter 1 to add an order amount, 2 to view all orders, q to quit: ")

# Task 4
daily = [200, 150, 0, 400, 50, -1, 300]
total_sales = 0
for sale in daily:
    if sale < 0:
        print("Corrupted data encountered. Stopping processing.")
        break
    elif sale == 0:
        print("No sales today.")
        continue
    total_sales += sale
    print(f"Total sale so far: {total_sales}")

print(f"Final Sales Amount: {total_sales}")
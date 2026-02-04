def add_price(price_list, price):
    price_list.append(price)
    return price_list   

def get_avg_price(price_list):
    if len(price_list) == 0:
        return 0
    return sum(price_list) / len(price_list)

def get_max_price(price_list):
    if len(price_list) == 0:
        return 0
    return max(price_list)

price_list = []
input = input("Enter 1 to add a price, 2 to get the average price, 3 to get the maximum price, 4 or q to exit: ")
while input != "4" and input != "q":
    if input == "1":
        try:
            price = float(input("Enter the price: "))
            add_price(price_list, price)
        except ValueError:
            print("Invalid price. Terminating program....")
            break
    elif input == "2":
        avg_price = get_avg_price(price_list)
        print(f"The average price is: {avg_price}")
    elif input == "3":
        max_price = get_max_price(price_list)
        print(f"The maximum price is: {max_price}")
    else:
        print("Invalid input. Please try again.")
    input = input("Enter 1 to add a price, 2 to get the average price, 3 to get the maximum price, 4 or q to exit: ")
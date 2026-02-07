# Task 5
cart= []

class NegativePriceError(Exception):
    pass

while True:
    try:
        input = input("Enter price for an item, or 'q' to quit: ")
        if input == "q":
            break
        price = float(input)
        if price < 0:
            raise NegativePriceError("Price cannot be negative.")
        cart.append(price)
    except ValueError:
        print("Invalid input. Please enter a valid price.")
        continue
    except NegativePriceError as e:
        print(e)
        continue
    
total = sum(cart)
print("total items in cart:", len(cart))
print(f"Total bill: ${total:.2f}")
# Task 2

prices = [120, 350, 'abc', 500, -200, 800]
sum=0

class NegativeException(ValueError):
    pass


for price in prices:
    try:
        if price < 0:
            raise NegativeException("Negative price encountered.")
        sum+=price
    except TypeError:
        print(f"Invalid price: {price}")
    except NegativeException as ne:
        print(ne)
    print(f"Current total: {sum}")

print(f"Final total: {sum}")
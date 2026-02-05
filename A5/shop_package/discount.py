def apply_discount(price, discount):
    if discount < 0 or discount > 1:
        raise ValueError("Discount must be between 0 and 1.")
    discounted_price = price * (1 - discount)
    return discounted_price

def flat_discount(price):
    discounted_price = price - 50
    return discounted_price
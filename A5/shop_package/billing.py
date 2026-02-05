def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def apply_tax(total):
    tax_rate = 0.05
    return total * (1 + tax_rate)
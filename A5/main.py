import math_utils as mth
from math_utils import square
import string_utils as str_utils
import shop_package.discount as disc
from shop_package.billing import calculate_total, apply_tax

## Task1
print(mth.add(5, 3))        # Output: 8
print(mth.subtract(10, 4))  # Output: 6
print(square(6))        # Output: 36

## Task2
print(str_utils.capitalize_string("hello"))  # Output: Hello
print(str_utils.reverse_string("world"))     # Output: dlrow
print(str_utils.word_count("This is a test string."))  # Output: 6

## Task 3 & 4
prices = [100, 200, 300]
total = calculate_total(prices)
total_with_tax = apply_tax(total)
print(f"Total before tax: {total}")
print(f"Total after tax: {total_with_tax}")

discounted_total = disc.apply_discount(total_with_tax, 0.1)  # Applying a 10% discount
print(f"Total after discount: {discounted_total}")
discounted_total_flat = disc.flat_discount(total_with_tax)  # Applying a flat discount of $50
print(f"Total after flat discount: {discounted_total_flat}")
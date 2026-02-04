def apply_discount(price, discount_percent=5):
    # optional
    if discount_percent > 60:
        discount_percent = 60
    discounted_price = price * (1 - discount_percent / 100)
    actual_price = price - discounted_price
    return actual_price

def test_apply_discount():
    assert apply_discount(1000,10) == 900
    assert apply_discount(500) == 475

test_apply_discount()


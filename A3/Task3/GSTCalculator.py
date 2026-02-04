gst_cal = lambda price: price + (price * 0.18)

# optional
apply_discount = lambda price, discount_percent=5: price * (min(discount_percent, 60) / 100)

total_with_gst = lambda price: gst_cal(price) - apply_discount(price)
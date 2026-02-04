gst_cal = lambda price: price + (price * 0.18)

prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst_cal, prices))

print("Original Prices:", prices)
print("With GST:", prices_with_gst)
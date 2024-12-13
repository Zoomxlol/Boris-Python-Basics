greening_price = 7.61
discount = 0.82

garden = int(input())
price = (greening_price * garden) * discount
discount_price = (greening_price * garden) - price
print(f"The final price is: {price:.2f} lv.")
print(f"The discount is: {discount_price:.2f} lv.")

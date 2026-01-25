# ternary operator

order_amount = int(input("Enter your order amount: "))

# print(type(order_amount))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is {delivery_fees}")
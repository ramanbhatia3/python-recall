# generator comprehensions for memory optimization

daily_sales = [5, 10, 12, 5, 15, 3, 12, 7, 10]

# total_cups = (sale for sale in daily_sales if sale > 5)

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
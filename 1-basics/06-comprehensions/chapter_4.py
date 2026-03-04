# dictionaries comprehensions

course_prices_inr = {
    "FSD": 2000,
    "AI": 3000,
    "CC": 6000
}

course_prices_usd = {course:price/80 for course,price in course_prices_inr.items()}

print(course_prices_usd)
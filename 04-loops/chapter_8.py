# using dictionary in place of match case

courses = [
    {"course": "FSD", "fee": 2000, "coupon": "P20"},
    {"course": "AI", "fee": 4000, "coupon": "F500"},
    {"course": "CC", "fee": 6000, "coupon": "P50"}
]

discounts = {
    "P20": (0.2,0),
    "F500": (0,500),
    "P50": (0.5,0)
}

for course in courses:
    percent, fixed = discounts.get(course["coupon"],(0,0))
    discount = course["fee"] * percent + fixed

    print(f"Discount of {discount} rupees on {course['course']} course till next Friday!!")
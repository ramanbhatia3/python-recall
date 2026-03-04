# Dictionary

dict1 = dict(f_name="Ramandeep",l_name="Bhatia",age=21)

print(f"Dict1 Order: {dict1}")

dict2 = {}

dict2["f_name"] = "Mohit"
dict2["l_name"] = "Bhatia"

print(f"Dict2 First Name: {dict2['f_name']}")

print(f"Dict2 Order: {dict2}")

del dict2["l_name"]

print(f"Dict2 Order: {dict2}")


# membership test

print(f"Is 'f_name' in Dict 2? {'f_name' in dict2}")
print(f"Is 'l_name' in Dict 2? {'l_name' in dict2}")



print(f"Dict1 Details (keys): {dict1.keys()}")
print(f"Dict1 Details (values): {dict1.values()}")
print(f"Dict1 Details (items): {dict1.items()}")




dict3 = dict(f_name="Mohit",l_name="Bhatia",age=22,language="JavaScript")

last_item = dict3.popitem()

print(f"Popped Item: {last_item}")


dict4 = {"course":"FSD","fees":5900}

dict1.update(dict4)

print(f"Updated Dict1 : {dict1}")

course_fee = dict1["fees"]

print(f"Training Fee : {course_fee}")

# course_marks = dict1["marks"] # error

# safe way

course_marks = dict1.get("marks", "No Marks")

print(f"Training Marks : {course_marks}") 

course_fee = dict1.get("fees", "No Fees")

print(f"Training Fee : {course_fee}") 
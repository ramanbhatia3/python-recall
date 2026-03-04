# functions

def name_and_course(name, course):
    print(f"{name} is enrolled in {course} course")


name_and_course("Raman","FSD")
name_and_course("Mohit","IT")




def bill_calculator(items,price):
    return items*price

bill1 = bill_calculator(3,25)
print("Bill 1: ",bill1)

bill2 = bill_calculator(10,15)
print("Bill 2: ",bill2)



# nested functions

def fetch_sales():
    print("Fetching Sales Data")

def filter_valid_sales():
    print("Filtering Valid Sales")

def summarize_data():
    print("Summarizing Data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


print("Report 1:")
generate_report()

print("Report 2:")
generate_report()
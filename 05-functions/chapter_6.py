# documenting your functions

def chai_name(name="Masala"):
    """Prints the chai name"""
    print(f"Serving you a {name} Chai")

print(chai_name.__doc__)  # __doc__ -> pronounced as dunder doc
print(chai_name.__name__)

# help(len)

def generate_bill(chai=0,samosa=0):
    """
    Calculate the total bill for chai and samosa
    
    :param chai: Number of chai cups (10 rupees each)
    :param samsosa: Number of samosas (15 rupees each)
    : return: (total amount, thank you message)
    """

    total = chai*10 + samosa*15
    return total, "Thank You for visiting!"
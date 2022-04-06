
# Alternative implementation of the calc_tax() function.
# Checking from highest target engine size to lowest (original checks from lowest to highest).
# Using '>=' to catch arguments with values greater than or equal to given conditions.

def calc_tax(engine_size):
    if engine_size >= 2000:
        return 1000
    elif engine_size >= 1500:
        return 750
    elif engine_size >= 1000:
        return 500
    else:
        return 250


# Print calculated tax of given engine size:
def print_tax(engine_size):
    print("The tax for the engine capacity", engine_size, "cc is €", calc_tax(engine_size))


# Test cases:
print_tax(878)  # Test 878 cc
print_tax(1000)  # Test 1000 cc
print_tax(1550)  # Test 1550 cc
print_tax(1998)  # Test 1998 cc
print_tax(2200)  # Test 2200 cc

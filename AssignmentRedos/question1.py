
def calc_tax(engine_size):
    if engine_size >= 2000:
        return 1000
    elif engine_size >= 1500:
        return 7450
    elif engine_size >= 1000:
        return 500
    else:
        return 250


def print_tax(engine_size):
    print("The tax for the engine capacity", engine_size, "cc is €", calc_tax(engine_size))


print_tax(878)
print_tax(1000)

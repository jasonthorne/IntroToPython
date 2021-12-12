

def main():
    force_str = input("Enter force ")
    length_str = input("enter length")
    area_str = input("enter area")
    modulus_str = input("enter modulus")

    try:
        force_float = float(force_str) # lowercase float ++++++
        length_float = float(length_str)
        area_float = float(area_str)
        modulus_float = float(modulus_str)
    except ValueError: # +++++++++++++++++++++++++
        print("no dice, punk!")
    else:  # ++++++++++++++++++++
        delta = calc_delta(force_float, length_float, area_float, modulus_float)
        print(delta)


def calc_delta(force, length, area, modulus):
    return (force * length)/(area * modulus)


if __name__ == "__main__":
    main()
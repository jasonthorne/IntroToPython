
# main function:
def main():
    # inform user of what the program does:
    print("This program calculates the change in length \u03B4 of an axially loaded metal rod.")

    # prompt user to input required values:
    force_str = input("Enter the force P (in N): ")  # store force input
    length_str = input("Enter the length L (in m): ")  # store length input
    area_str = input("Enter the area A (in m\u00B2): ")  # store area input
    modulus_str = input("Enter Young's modulus E (in Nm\u207B\u00B2): ")  # store modulus input

    try:  # try parsing inputted string values to floats:
        force_float = float(force_str)  # parse force input
        length_float = float(length_str)  # parse length input
        area_float = float(area_str)  # parse area input
        modulus_float = float(modulus_str)  # parse modulus input
    except ValueError:  # value error thrown on one or more invalid values:
        # inform user of error:
        print("There is a problem with one of your inputs. ALL inputs should be floating point numbers.")
    else:  # all values were successfully parsed:
        # calculate the delta, using parsed values:
        delta = calc_delta(force_float, length_float, area_float, modulus_float)
        # output delta value to user:
        print("The calculated change in length \u03B4 is", delta, "m.")


# calculate delta function:
def calc_delta(force, length, area, modulus):
    # calculate and return the change in length δ of an axially loaded metal rod:
    return (force * length)/(area * modulus)


# if module is run as script (i.e: name == "__main__"):
if __name__ == "__main__":
    main()  # execute main function

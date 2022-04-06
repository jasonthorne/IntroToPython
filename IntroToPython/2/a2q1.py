
from random import choice  # import 'choice' function from 'random' module


# main function:
def main():
    # inform user of what the program does:
    print("This program picks a random item from a list of items input by the user.")

    # prompt user to input a string of items, separated by '/':
    items_str = input("Enter your items separated by a / : ")

    # create list of items from string, splitting by '/':
    items_list = items_str.split("/")

    # show user their list of items:
    print("The items you entered are:", items_list)

    # show a random item, using imported choice function:
    print("Picking an item at random:", choice(items_list))


# if module is run as script (i.e: name == "__main__"):
if __name__ == "__main__":
    main()  # execute main function

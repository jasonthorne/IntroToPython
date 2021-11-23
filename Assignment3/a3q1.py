
from random import shuffle  # import 'shuffle' function from 'random' module


# main function:
def main():
    # inform user of what the program does:
    print("This program accepts a sequence of user inputs, and prints them to the console in random order.")

    item = None  # holds an inputted item
    items_list = []  # holds inputted items

    while item != "done":  # while item variable doesn't hold value of 'done':
        # prompt user to input an item, or 'done' to stop:
        item = input("Enter an item, or \"done\" to stop entering items: ")

        if item != "done":  # if user hasn't entered 'done':
            items_list.append(item)  # add item to list of items

    items_as_str(items_list)  # pass list of items to 'items_as_str()'


# items_as_str function:
def items_as_str(items_list):
    # print items in order of input:
    print("Your items in original order: ", end="")
    for item in items_list:  # loop through each item in list
        print(item, "", end="")  # print current item

    # print items in random order:
    print("\nYour items in random order: ", end="")
    shuffle(items_list)  # shuffle list items using imported 'shuffle' function
    for item in items_list:  # loop through each item in list
        print(item, "", end="")  # print current item


# if module is run as script (i.e: name == "__main__"):
if __name__ == "__main__":
    main()  # execute main function

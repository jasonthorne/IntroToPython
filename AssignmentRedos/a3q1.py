from random import shuffle


def main():

    item = None
    items_list = []

    while item != "done":
        item = input("Enter item, or 'done' to stop")

        if item != "done":
            items_list.append(item)  #++++++++++++append()

    items_as_str(items_list)


def items_as_str(items_list):
    print("items in original order:")
    for item in items_list:
        print(item, "", end="") #++++++++++++++++++

    print("\nitems in random order:")
    shuffle(items_list)
    for item in items_list:
        print(item, "", end="")


if __name__ == "__main__":
    main()
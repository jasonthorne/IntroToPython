from random import choice


def main():
    items_str = input("Enter your items, separated by '/'")

    items_list = items_str.split("/")

    print("the items you entered are", items_list)

    print("picking an item at random:", choice(items_list))


if __name__ == "__main__":
    main()

import argparse
import decimal


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("input_file", type=str, help="path to input file")

    input_file = None
    data_dict = {"rain": [], "temp": [], "sun": []}

    try:
        input_file = open(parser.parse_args().input_file, "rt", encoding="utf8")

        for data_row in input_file.readlines()[24:]:  # loop through each row of data
            data_list = data_row.split(",")  # split data row by ',' into list of data

    parser = argparse.ArguementParser()
    parser.add_argument("input_file", type=str, help="help msg")

    try:
        input_file = open(parser.parse_args().input_file, "rt", encoding="utf8")

        for data_row in input_file.readlines():
            print("yo")

    except:





if __name__ == "__main__":
    main()
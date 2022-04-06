import argparse  # import 'argparse' module
import decimal  # import 'decimal' module


# main function:
def main():
    # create ArgumentParser object:
    parser = argparse.ArgumentParser()

    # create positional command line argument 'input_file':
    parser.add_argument("input_file", type=str, help="specify path to input file")

    input_file = None  # holds input file
    data_dict = {"rain": [], "temp": [], "sun": []}  # holds data of target values

    try:
        # try to open input_file with parsed arg path given by user:
        input_file = open(parser.parse_args().input_file, "rt", encoding="utf8")

        index_dict = {}  # holds indexes of target values
        index = 0  # holds index value

        # loop through values on header row, split by ','
        for value in input_file.readlines()[23:24][0].split(","):
            if value in data_dict.keys():  # if value is a target value
                index_dict.update({value: index})  # update index_dict with value and it's index
            index += 1  # increment index

        # reset file's read cursor to start of file:
        input_file.seek(0)  # https://docs.python.org/2.4/lib/bltin-file-objects.html

        for data_row in input_file.readlines()[24:]:  # loop through each row of data
            data_list = data_row.split(",")  # split data row by ',' into list of data

            for value in data_dict.keys():  # for each target value name in data_dict:
                # append matching list with decimal cast value from data_list at matching index from index_dict:
                # casting data to decimal for increased precision: https://docs.python.org/3/library/decimal.html
                data_dict.get(value).append(decimal.Decimal(data_list[index_dict.get(value)]))

    except FileNotFoundError:  # throw 'FileNotFoundError' if file not found
        print("Error: File not found")  # inform user of error
    finally:
        for data_list in data_dict.values():  # for each list in data_dict:
            data_list.sort(reverse=True)  # sort values by highest to lowest

        if input_file is not None:  # if file was opened (not None):
            input_file.close()  # close input_file

    # variables for queries:
    rainfall_total = decimal.Decimal(0)  # holds total of all rainfall
    rainfall_hours = 0  # holds hours of rainfall over 5mm
    temp_max = decimal.Decimal(0)  # holds maximum temperature
    sun_total = decimal.Decimal(0)  # holds total of all sunshine

    # loop through data_dict's rain data:
    for rain_data in data_dict.get("rain"):
        if rain_data == 0.0:  # if a value is 0.0:
            break  # break as all further values are 0.0
        rainfall_total += rain_data  # add rain data to sum of rainfall
        if rain_data > 5.0:  # if rain data was over 5.0:
            rainfall_hours += 1  # increment rainfall_hours

    # loop through data_dict's temp data:
    for temp_data in data_dict.get("temp"):
        if temp_data == 0.0:  # if a value is 0.0:
            break  # break as all further values are 0.0
        if temp_data > temp_max:  # if temp data > current max
            temp_max = temp_data  # store data as new max

    # loop through data_dict's sun data:
    for sun_data in data_dict.get("sun"):
        if sun_data == 0.0:  # if a value is 0.0:
            break  # break as all further values are 0.0
        sun_total += sun_data  # add sun data to sum of sun

    # show total amount of rainfall over all data:
    print(f"Q1 - Total rainfall over all data points: {rainfall_total} mm")
    # show total hours of rainfall over 5mm:
    print(f"Q2 - Number of hours where rainfall was over 5mm: {rainfall_hours}")
    # show maximum temperate:
    print(f"Q3 - Maximum temperature ever recorded: {temp_max} degrees")
    # show average sunshine using sun_total/length of sun data:
    print(f"Q4 - Average sunshine over all data points: {sun_total/len(data_dict.get('sun')):.4f}")


# if module is run as script (i.e: name == "__main__"):
if __name__ == "__main__":
    main()  # execute main function

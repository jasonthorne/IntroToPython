
def calc_grade(mark):
    if mark < 40:
        return "E"
    elif mark < 50:
        return "D"
    elif mark < 60:
        return "C"
    elif mark < 70:
        return "B"
    else:
        return "A"


def print_grade(mark):
    print("The grade letter for mark ", mark, "is", calc_grade(mark))


print_grade(55)
print_grade(90)
print_grade(10)

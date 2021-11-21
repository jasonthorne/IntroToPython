# ==================================================================
# Original function:

# def calc_grade(n):
#     if n <= 40:
#         return "E"
#     elif n < 50:
#         return "D"
#     elif n <= 60:
#         return "C"
#     elif n is 70:
#         return "A"

# ==================================================================
# Bugs found in original function:
# ------------------------------------------------------------------
# Bug 1:
# Mark of 40 returns 'E' instead of 'D' grade.
# ------------------------------------------------------------------
# Bug 2:
# Marks from 60-69 should return a 'B' grade.
# 2a - Mark of 60 instead returns a 'C' grade.
# 2b - There are no expressions to catch marks from 61-69.
# ------------------------------------------------------------------
# Bug 3:
# Comparison for mark of 70 checks for reference instead of value.
# ------------------------------------------------------------------
# Bug 4:
# There is no expression to catch marks over 70.
# ==================================================================

# Fixed function:
def calc_grade(mark):
    if mark < 40:  # Bug 1 fixed
        return "E"
    elif mark < 50:
        return "D"
    elif mark < 60:  # Bug 2a fixed
        return "C"
    elif mark < 70:  # Bug 2b fixed
        return "B"
    else:  # Bugs 3 & 4 fixed
        return "A"


# Print calculated grade of given mark:
def print_grade(mark):
    print("The grade letter for the mark", mark, "is", calc_grade(mark))


# Test cases:
print_grade(35)  # Test mark of 35
print_grade(44)  # Test mark of 44
print_grade(52)  # Test mark of 52
print_grade(65)  # Test mark of 65
print_grade(88)  # Test mark of 88

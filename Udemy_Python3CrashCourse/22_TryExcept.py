# exception from 1 / 0:

try:
    1/0
except Exception as e: # catch exception
    print(e) # print exception
    print(type(e)) # print exception type

# -----------------------

try:
    1/0
    print("IM NOT EXECUTED :P")
except ZeroDivisionError: # catch spcific exception
    print("computer say's no!")


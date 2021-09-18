
# return:

def function1():
    return "returned string"

print(function1()) # call function

# --------------------------------------

# param:

def function2(name):
    print(f"Hullo, {name}!")


function2("sexy") # call function

# --------------------------------------

# default param: - known as a KEYWORD arguement

def function3(name, greeting = "Hullo"): # +++++++ if second param not given default is used
    # greeting = "new greeting" # value can just be assigned here as normal too :P
    print(f"{greeting}, {name}!")


function3("sexy") # use default 2nd param
function3("sexy", "yo") # provide second param

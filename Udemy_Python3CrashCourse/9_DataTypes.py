# DICTIONARIES - objects with key: value pairs:

person = {
    "name" : "Jason", # string key val pair
    3 : 333 # int key val pair
}

print(person); # print whole obj
print(person["name"]) # print val for name key
print(person[3]) # print int value for int key

# -------------------------------
# TUPLES - Like lists, but uses perenthesis, which makes list final.

myList = ["listItem1", "listItem2"];
print(myList);

myList.append("listItem3"); # lists can be changed
print(myList);


myTuple = ("tupleItem1", "tupleItem2");
print(myTuple);
# myTuple.append("tupleItem3"); # falls over as tuple CANT be changed 

# -------------------------------
# SETS - unique lists (only one of each element allowed):

mySet = {1, 2, 1, 1, 3, 2};
print(mySet); # only 1 '1 ' & 1 '2'
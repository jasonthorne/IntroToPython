# TRADITIONAL FORMATTING:

name = "Jason";
message1 = "{} is my name".format(name); # .format injects name into braces
print(message1);

# -------------------------------
# F STRINGS:

message2 = f"{name} is my name"; # inject name into name. (NOTE - leading 'f' before string)
print(message2);
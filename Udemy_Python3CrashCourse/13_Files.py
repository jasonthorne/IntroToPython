
# -------------------------------
# CREATE & WRITE TO FILE:

# create new file using 'with' keyword
# open() opens the file, and returns it as a file object
# 'w' means file is opened with write permissions
# fileHandler is opject that helps us manage the file

with open("myNewFile.py", "w") as fileHandler1:
    fileHandler1.write("print('Sup, World!')");
    fileHandler1.close; # close file handler IMPORTANT :P 

# -------------------------------
# READ FILE:

# 'r' is read permissions

with open("myNewFile.py", "r") as fileHandler2:
    fileContent = fileHandler2.read();
    fileHandler2.close; # close file handler IMPORTANT :P

print(fileContent);

# -------------------------------
# APPEND TO FILE:

# 'r' is append permissions

with open("myNewFile.py", "a") as fileHandler3:
    fileHandler3.write("\nappended to file on new line"); # add appended text
    fileHandler3.close; # close file handler IMPORTANT :P

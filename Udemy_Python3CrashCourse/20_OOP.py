
# class:
class Person1:
    name = "Jason"
    
    # method needs 'self' passed in as first arg to bind it to class +++++++++++
    def speak(self):
        print("Jason speaks!")


me = Person1()
print(me.name) # print name
me.speak() # invoke method

# -------------------

# class with constructor:

class Person2:
    def __init__(self, name, age): # +++++++++++Constructor here MUST be written as __init__ (2 underscores on each side)
        self.name = name
        self.age = age
    
    def get_name(self):
        print("name is: ", self.name)
        
    def get_age(self):
        print(f"age is: {self.age}")
        
    def __str__(self): # override to string (I think! :P)
        return self.name

me2 = Person2('Jason', '38')
me2.get_name()
me2.get_age()
print(me2)
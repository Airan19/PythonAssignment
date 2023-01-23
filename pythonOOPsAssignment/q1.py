"""
Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog
"""

# Here's the Animal Base class
class Animals:

    # Initializing the Class or Constructing the class object with parameter name i.e __init__ acts as the constructor 
    def __init__(self, name, canBark=False): 
        self._name = name     # assigning the name to the object
        self.canBark = canBark  # this attribute will be directly accessible unlike self._name which is protected attribute

    # If in any case user want to change the name, then set_name method will provide the functionality
    def set_name(self, name):
        self._name = name

    # User can get the name of the object by calling this method or else he/she can directly refer to object.name,
    # This method will be handy incase of private and protected attributes
    def get_name(self):
        return self._name


class Cow(Animals):
    def __init__(self, name, canFly):
        super().__init__(name)
        self.canFly = canFly


class Horse(Animals):
    def __init__(self, name,  canFly):
        super().__init__(name)
        self.canFly = canFly


class Dog(Animals):
    def __init__(self, name, canFly, canBark):
        super().__init__(name, canBark)
        self.canFly = canFly


c = Cow('Cow', False)                             # Creating object of class Cow
print(c.get_name(), c.canBark)                    
h = Horse('Horse', False)                         # Creating object of class Horse
print(h.get_name(), h.canBark)
d = Dog('Dog', False, True)                       # Creating object of class Dog
print('Can '+d.get_name()+' bark:', d.canBark)    

d.set_name('Vee')                                 # Setting new name for above created dog object
print('Name of Dog 1 is ',d.get_name())

print('Can cow fly:',c.canFly)

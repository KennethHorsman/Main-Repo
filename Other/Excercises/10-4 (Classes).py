#pylint: disable=missing-class-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=trailing-whitespace
#pylint: disable=invalid-name

'''
Design a class named Computer that holds the make, model, 
and amount of memory of a computer. Include methods to set 
the values for each data field, and include a method that 
displays all the values for each field. Create the class diagram 
and write the pseudocode that defines the class.'''

class Computer:
    def __init__(self, make=None, model=None, memory=None):
        self.make = make
        self.model = model
        self.memory = memory
        
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model
        
    def set_memory(self, memory):
        self.memory = memory
        
    def display(self):
        for field in ("make", "model", "memory"):
            value = getattr(self, field)
            if value is not None:
                print(f"{field.title()}: {value}")
        
computer = Computer()
computer.set_make("Lenovo")
computer.set_model("IdeaPad 3i")
computer.set_memory("8GB")
computer.display()

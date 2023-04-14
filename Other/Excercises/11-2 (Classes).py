#pylint: disable=missing-class-docstring
#pylint: disable=missing-function-docstring
#pylint: disable=trailing-whitespace
#pylint: disable=invalid-name
#pylint: disable=line-too-long
'''
a. Design a class named PhoneCall with four fields: 
two strings that hold the 10-digit phone numbers that originated and received the call, 
and two numeric fields that hold the length of the call in minutes and the cost of the call. 
Include a constructor that sets the phone numbers to Xs and the numeric fields to 0. 
Include get and set methods for the phone number and call length fields, but do not include a 
set method for the cost field. When the call length is set, calculate the cost of the call at 
three cents per minute for the first 10 minutes, and two cents per subsequent minute. 

b. Design an application that declares three PhoneCalls. Set the length of one PhoneCall 
to 10 minutes, another to 11 minutes, and allow the third object to use the default value 
supplied by the constructor. Then, display each PhoneCall's values.

c. Create a child class named InternationalPhoneCall that inherits from PhoneCall. Override the 
parent class method that sets the call length to calculate the cost of the call at 40 cents per minute.

d. Create the logic for an application that instantiates a PhoneCall object and an 
InternationalPhoneCall object and displays the costs for each.
'''

class PhoneCall:
    def __init__(self, caller="x", receiver="x", length=0):
        self.caller = caller
        self.receiver = receiver
        self.length = length
        
    @property
    def caller(self):
        return self._caller
    
    @caller.setter
    def caller(self, value):
        self._caller = value

    @property
    def receiver(self):
        return self._receiver
    
    @receiver.setter
    def receiver(self, value):
        self._receiver = value
        
    @property
    def length(self):
        return self._length
        
    @length.setter
    def length(self, length):
        if length is not None:
            try:
                self._length = float(length)
                self.calculate_cost()
            except ValueError:
                self._length = 0
                self.cost = 0
        else:
            self._length = 0
            self.cost = 0
            
    def calculate_cost(self):
        if self._length <= 10:
            self.cost = self._length * 3
        else:
            self.cost = 10 * 3 + (self._length - 10) * 2

def get_valid_phonenumber(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.replace('-', '')
        if len(user_input) == 10 and user_input.isdigit():
            return user_input
        else:
            print("The phone number must only contain numbers, or dashes where applicable.")   
        
def get_number_calls():
    while True:
        number_calls_input = input("Please enter the number of calls: ")
        if number_calls_input.isdigit():
            return int(number_calls_input)
        else:
            print("The number of calls must be a positive number only.")
        
def get_reciever_number():
    return get_valid_phonenumber("Enter the receiver number: ")
    
def get_caller_number():
    return get_valid_phonenumber("Enter the caller number: ")
    
def get_length():
    while True:
        length_input = input("Enter the call length in minutes: ")
        if length_input is not None:
            try:
                return float(length_input)
            except ValueError:
                pass
        print("The call length must be a positive number only.")

number_calls = get_number_calls()

calls = [(get_caller_number(), get_reciever_number(), get_length()) for _ in range(number_calls)]

for i, call in enumerate(calls):
    phone_call = PhoneCall(*call)
    print(f"The cost of call {i+1}, from {phone_call.caller} to {phone_call.receiver}, is {int(phone_call.cost) if phone_call.cost.is_integer() else phone_call.cost} cents.")

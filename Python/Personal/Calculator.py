import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

# operator_input = "+"
# number1 = 4
# number2 = 2
# print(ops[operator_input](number1,number2))


user_input = input("Enter equation: ").replace(" ", "")

myOperators = [x for x in user_input if x in ("+-*/")]

new_list = []
for x in user_input:
    if x.isnumeric():
        new_list.append(int(x))
    elif x in myOperators:
        new_list.append(x)
    else:
        pass

new_list_copy = new_list[0:]
operatorIndex = []
for x in myOperators:
    operatorIndexes = new_list_copy.index(x)
    operatorIndex.append(operatorIndexes)
    new_list_copy[operatorIndexes] = f"ops: {x}"
    



    
print("new list: ", new_list)
print("ops: ", myOperators)
print("ops index: ", operatorIndex)

# Find indexes of operators, join elements in data_list around operator. Use Try Except to see if element calculation is possible?

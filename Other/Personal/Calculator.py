import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

operator_input = "+"
number1 = 4
number2 = 2

print(ops[operator_input](number1,number2))


data_list = []
user_input = input("Enter equation: ").replace(" ", "")
for x in user_input:
    data_list.append(x)
print(data_list)


myIntList = [x for x in data_list if x.isnumeric()]
myOperators = [x for x in data_list if x in ("+-*/")]
operatorIndex = []
for x in myOperators:
    operatorIndexes = data_list.index(x)
    operatorIndex.append(operatorIndexes)
    data_list[operatorIndexes] = F"operator: {x}"

print("original data_list: ", data_list)
print("int data_list: ", myIntList)
print("ops data_list: ", myOperators)
print("ops index data_list: ", operatorIndex)

# Find indexes of operators, join elements in data_list around operator. Use Try Except to see if element calculation is possible?

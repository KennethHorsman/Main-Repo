list = []
user_input = input("Enter equation: ").replace(" ", "")
for x in user_input:
    list.append(x)
print(list)


myIntList = [x for x in list if x.isnumeric()]
myOperators = [x for x in list if x in ("+-*/")]
operatorIndex = []
for x in myOperators:
    operatorIndexes = list.index(x)
    operatorIndex.append(operatorIndexes)
    list[operatorIndexes] = F"operator: {x}"

print("original list: ", list)
print("int list: ", myIntList)
print("ops list: ", myOperators)
print("ops index list: ", operatorIndex)

# Find indexes of operators, join elements in list around operator. Use Try Except to see if element calculation is possible?

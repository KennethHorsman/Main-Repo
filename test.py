import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

import re
 
# initializing string
test_str = "45 + 98-10"
 
# printing original string
print("The original string is : " + test_str)
 
# Expression evaluation in String
# Using regex + map() + sum()
res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))
 
# printing result
print("The evaluated result is : " + str(res))
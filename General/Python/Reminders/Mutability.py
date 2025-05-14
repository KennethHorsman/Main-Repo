def f2(c,d):
    print(c) # Statement 1
    c.append(0)
    print(d) # Statement 2
def f1(a,b):
    b = b + 1
    f2(a,b)
    print(f"b: {b}")
    b = b + 1
    print(f"b: {b}")
    print(f"a {a}")
i = [10,5]
j = 0
f1(i, j)
print(i) # Statement 3
print(j) # Statement 4

'i = a = c'
'j = b = d'
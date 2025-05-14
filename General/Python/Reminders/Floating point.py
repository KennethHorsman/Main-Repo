from decimal import Decimal

total = Decimal(0.0)

for i in range(0,10):
    v = Decimal(input("Enter a value: "))
    total = total + v
    print(total)
if total < 1.0:
    print("Your total is less than 1.0")
elif total == 1.0:
    print("Your total is exactly 1.0")
else:
    print("Your total is greater than 1.0")
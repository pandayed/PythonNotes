age = 19
if age>=18:
    print("Adult")
elif age>=45:
    print("Too Adult")
else:
    print("Whatever but not adult")

# in python we cannot use tabs in place of spaces and vice versa
x=10
# if block can not be empty so we use pass keyword
if x>1:
    pass
else:
    print("do something")

# logical operators
# and
# or
# not
x = 100
y = 20
if not x>y:
    print("x is not greater than y")
else:
    print("x is greater than y")

if x>y and x>10:
    print("x is greater than y and x is greater than 10")

if x>y or x>10:
    print("x is greater than y or x is greater than 10")

# chaining of operators
if 10<x<20:
    print("x lies between 10 and 20")


# ternary operator
age = 20
message = "Eligible" if age>=18 else "Not elegible"
print(message)
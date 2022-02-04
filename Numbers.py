import math

import main


x = 10

# 0b prefix is used for binary representation
y = 0b101
print(y)

# bin function gives binary representation of a number
print(bin(x))

# 0x for hexadecimals
z = 0x12c

# hex fun returns hex representation
print(hex(x))

# complex numbers
a = 1+2j # j or J represents imaginary part
print(a)

# Arithmetic Operators
x = 10 + 20
print(x)
x = 10 - 2
print(x)
x = 10 * 2
print(x)
x = 10 % 2
print(x)

# there are two types of division
x = 10/3 # gives decimal answer
print(x)
x = 10 // 3 # gives int answer
print(x)

# left to the power of right
x = 10 ** 2
print(x)

# augmented assignment operators
x+=1
x-=1
x/=2
x*=2

# in python we do not have increment and decrement operators

# in python we do not have constants, all we have are variables

# but conventionally we use uppercase for variables of which values should not be modified
PI= 3.14 # we can modify PI we should not

x = 3.145
print(round(x)) # rounds off to integer
x=-10
print(abs(x)) # prints absolute value

# whenever you search for something in python use the version of python

# using math module
print(math.floor(3.14))
print(math.ceil(3.14))

# type conversion
# input in python is received as string so we need to convert that
# since the input are not implicitly converted, python and such languages are called strongly typed languages
# languages which do auto type conversion of input are called weakly typed languages
x = input("x: ")
print(x)

# type conversions
print(int(x))
print(float(x))
print(bool(x))


# false values in python
# empty string i.e. ""
# 0
# empty list i.e. []
# None # None is like NULL in cpp
# except these all are true
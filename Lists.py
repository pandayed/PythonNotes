# lists are enclosed in []
names = ["lal", "bihari", "pandey"]

# list of lists
matrix = [[1, 2, 4], [3], [4,5]]

# list of 5 zeroes
zeros = [0]*5
print(zeros)

# lists can have mutliple datatype items
list1 = [10, "a"]

# conatenating lists
combination = list1 + zeros
print(combination)

# list function: it takes an iterable
list3 = list(range(2, 10))
print(list3)

mychars = list("Lal Bihari Pandey")
print(mychars)

# len function
print(len(mychars))

# accessing items in a list
print(mychars[0], mychars[-1])

# slicing
# slicing does not affect the original iterable
print(mychars[11:])
print(mychars[3:11:2])
print(mychars[::2])
# reading items in reverse order
print(mychars[::-1])


# Lists Unpacking
numbers = [1, 2, 3]
# number of variables on left must be equal to number of items in list
one, two, three = numbers

# to get only first few elements
# remaining will be a list of remaining elements
first , second, *remaining = numbers

first, *between, last = numbers


# looping over lists
for name in names:
    print(name)

# getting index with item
# enumerate return tuple of two items
for name in enumerate(names):
    print(name)
    print("index " + str(name[0]) + " name " + str(name[1]))

# getting indices this way is ugly so we use list unpacking
for index, name in enumerate(names):
    print(index, name)
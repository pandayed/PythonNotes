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
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


# adding items to list
fruits = ["apple", "banana"]
print(fruits)
# insertion at end
fruits.append("guava")
print(fruits)
# insertion at given index
fruits.insert(0, "Grapes")

# removing
# at end
# for removal at end use pop without passing index
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)
# removes the first occurrence of the value
fruits.remove("banana")
# to remove all the instances of a value iterate over the list

#del : to remove item at an index or over a range
fruits = ["apple", "banana", "guava", "grapes", "papaya", "anaar"]
del fruits[1]
print(fruits)
del fruits[2:4]
print(fruits)

# deleting all objects in a list
fruits.clear()

# finding items
fruits = ["apple", "banana", "guava", "grapes", "papaya", "anaar"]
print(fruits.index("apple"))
# trying to find something which does not exist gives error called ValueError
# most of the languages return -1 but python does not
# print(fruits.index("orange")) # this gives error

# so before finding index one must check if the item exists
if "orange" in fruits:
    print(fruits.index("orange"))

# to get number of occurrences of the element
print(fruits.count("apple"))
print(fruits.count("orange"))
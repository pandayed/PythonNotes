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


# sort
nums = [2, 2, 16, 78 ,3]
# in ascending
nums.sort()
print(nums)
# in descending
nums.sort(reverse=True)
print(nums)

# sorted does not modify the original list
# it returns a list which is sorted
nums2 = sorted(nums)
print(nums2)
nums3 = sorted(nums, reverse=True)
print(nums3)

# sorting comples lists
items = [
    ("i1", 10),
    ("i2", 0)
]

items.sort()
print(items)
# nothing changes in this case because python does not know how to sort this


# this fun will tell python that list should be sorted on the basis of element at index 1 in tuple
def sorter(item):
    return item[1]

items.sort(key=sorter)
print(items)


# lambda functions : simple, one lined, anonymous functions
# lambda keyword is used
# syntax: lambda parameter:return statement
items.append(("i3", -10))
items.sort(key= lambda item:item[1])
print(items)

# let us say we want to create a list of numbers from the existing list
# basically we want to extract all the nos. from items and store them in a diff list

# we can use map function here
# map(list, lambda fun)

items = [
    ("item3", 3),
    ("item2", 2),
    ("item1", 1)
]
nos = map(lambda num: items[1], items)
print(nos)
# map fun returns map object
# to convert iterable into a list we use list fun
nosList = list(map(lambda item: item[1], items))
print(nosList)
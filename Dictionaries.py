from sys import getsizeof

# Dictionaries are basically maps

# x and y are keys and 1 and 2 are values
# keys must be of immutable type and values can be mutable or immutable
point = {"x":1, "y":2}

# dict fun
# dict fun takes one or more keyword arguments
point = dict(x=1, y=2)
print(point["x"])
point["z"] = 10
# we cannot access items in dictionary using numeric indices

# accessing unexisting key will give error so there are two ways to avoid error
# 1 check before accessing
if "a" in point:
    print("Present")

# 2 using get method
# get return none if key is unavailable
# we can also pass a default value to get fun to get in instead of none
print(point.get("a"))
# get with default value
print(point.get("a", -100))

# del
del point["x"]

# only keys are accssed
# x is basically key
for x in point:
    print(x)

for key in point:
    print(key, point[key])

# items fun for dictionaries
# each item is a tuple
for item in point.items():
    print(item)

# unpacking tuple
for key, value in point.items():
    print(key, value)


# Dictionaries Comprehension
# Comprehensions are same as lists for set and dictionaries, just the brackets differ

myList = [x*2 for x in range(5)]
print(myList)
mySet = {x*2 for x in range(5)}
print(mySet)
myDict = {x: x*2 for x in range(5)}
print(myDict)

# Generator Expressions
# when we use () in comprehensions generator expressions are returned
# Generator expressions do not store all the values but when we iterate them they spit out a value on each iteration
# they are used when we have a large or infinite data set
# since they do not store all the values we cannot get the len of the generator expressions

values = (x*2 for x in range(10000))
# print(len(values)) # error will be thrown
# but we can get the size
print(getsizeof(values))

# we cannot print the whole expression at a time but we can iterate and access elements one by one
for x in values:
    print(x)
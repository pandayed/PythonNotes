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

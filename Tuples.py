# tuple is read only list
point = (1, 2)
print(type(point))
# value with trailing comma is considered tuple
pointX = 1,
print(type(pointX))
# concatenating tuple
points = (1, 2) + (3, 4)
print(points)
# repeating tuple
points = (1, 2) * 3
print(points)
# converting iterable to tuple
myTuple = tuple("Lal")
print(myTuple)
# tuples are read only iterable so we can do everything on tuple which does not try to modify the tuple
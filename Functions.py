def sayMyName():
    print("Lal Bihari Pandey")


# you should have two line breaks after any function
def takeNameSayName(fName, lName):
    print(fName+" " + lName)
    return "Mid Name"


sayMyName()
takeNameSayName("lal", "pandey")

# by default all functions return None
print(sayMyName())
print(takeNameSayName("lal", "pandey"))

# we can return multiple values in python
def returnDob():
    return (7, "Sep" ,2001)


# in case of multiple return values a tuple is returned
# a tuple is read only list
# a tuple is enclosed in ()
myTuple = (1, 2, "Name")
print(returnDob())

# keyword arguments
# TODO

def defaultName(fName, lName="Pandey"):
    print(fName + lName)


defaultName("Lal Bihari")


# fun with explicit mentions
def myFun(a: int, b) -> tuple:
    return (a, b)
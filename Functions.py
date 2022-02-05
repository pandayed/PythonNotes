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
print("Keyword arguments called")
takeNameSayName(lName = "Pandey", fName = "Lal")

def defaultName(fName, lName="Pandey"):
    print(fName + lName)


defaultName("Lal Bihari")


# fun with explicit mentions
def myFun(a: int, b) -> tuple:
    return (a, b)

# arguments xarg for arbitrary number of arguments
# in case of xarg the values are received in tuple
def adder(*nums):
    print(nums)
    total = 0
    for x in nums:
        total+=x
        print(x)
    return total



print(adder(1,2,3,4))



# Arguments xxarg
# xxargs are received as key value pairs
def myFullName(**names):
    print(names)
    # key is put in double quotes
    print(names["fName"])
    print(names["mName"])


myFullName(fName="Lal", mName="Bihari", lName = "Pandey")


# there are two types of scope in python : local and global
# local variables
# if a variable is defined in a function it is accessible in the function after its definition
# there is nothing like block scope
def localVariableExample():
    if 10<20:
        localVariable = "Some message"

    if False:
        localVar2 = "Message"
    # locanVar 2 is not defined actually so it is not accessible outside
    print(localVariable)
    # print(localVar2) # this will generate error


localVariableExample()


var1 = "Var1"
var2 = "Var2"
def variableScopeExample():
    # a new var1 is created for this fun
    var1 = "Var 1 of fun"

    # this is the global var2
    global var2
    var2 = "Var 2 in fun but global"


# modifying global variables inside functions is not a good practice because other fun may depend on original value
# so do not use global statement in functions
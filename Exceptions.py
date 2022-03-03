

# when unable to convert input value into req datatype we get Value Error exception
try:
    num = int(input("Age: "))
except ValueError:
    print("The value cannot be converted to integer")


try:
    num = int(input("Age: "))
except ValueError:
    print("The value cannot be converted to integer")
else:
    print("Else gets executed when no exception is caught")

#storing exception in a variable
try:
    num = int(input("Age: "))
except ValueError as myExceptionVar:
    print("The value cannot be converted to integer")
    print(myExceptionVar)
    print(type(myExceptionVar))
else:
    print("Else gets executed when no exception is caught")
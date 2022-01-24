students_count = 10
rating = 4.9
is_it_raining = False
my_name = "Lal Bihari Pandey"

# initialization in same line
x, y, z = 1, 2, 3 # x is 1 y is 2 and z is 3

# this also works
a = b = 1

# in terms of typing there are two types of programming languages
# 1. Static : C++, C#, Java etc. # datatype must be explicitly mentioned # datatypes are determined at compile time
# 2. Dynamic: JavaScript, Ruby, Python etc. # no need to explicitly mention datatype # datatypes are determined at runtime

# to know datatype of a variable
print("Printing Datatypes")
print(type("My Name"))
print(type(1))
print(type(1.1))
print(type(False))


# the datatype of variable can be changed
my_var = 10
my_var = "Hey"

# explicit mention of datatypes
my_var1: int = 20
print(my_var1)
my_var1 : str = "Hello"
print(my_var1)

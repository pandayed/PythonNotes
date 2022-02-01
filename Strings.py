myName= "Lal Bihari Pandey"
# len function works for many containers
print(len(myName))
print(myName[0])

# negative index also works in python. -n gives nth character from last.
print(myName[-2])

# colon is used to slice
# first_index(inclusive) : second_index(exclusive)
# by default : first_index = 0 and second index = length
print(myName[2:6])
print(myName[:6])
print(myName[2:])
print(myName[:])

# whenever we access individual characters or use a part of string the characters are copied from string to some other memory location
print(id(myName))
print(id(myName[0]))

# Escape Sequences
# Printing Double Quotes

# single quotes also work
# in this case we can directly print double quotes
message = 'Python is cool'
message = 'Python is "Cool"'
print(message)

# writing strings in '' is not good
# we have escape sequences for that

escapeSequences = "\'  \"  \\  \n"
print(escapeSequences)

# triple quotes
multiLineString = """Here
 I
 am"""
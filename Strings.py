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

# concatenation works but we have

first = "Lal"
mid = "Bihari"
full = f"{first} {mid}" # F or f both work # f prefix means formatted string
print(full)

# we can put any expression in curly braces

print(f"{2+3}")

# some useful string methods
myName = "Lal Bihari Pandey"
print(myName.upper())
print(myName.lower())
print(myName.title()) # first letter of every word is capitalised # used in blog post titles

# remove extra white sapces
whiteSpaced = "  Word  "
print(whiteSpaced.strip()) # the string itself remains unchanged
print(whiteSpaced.lstrip())
print(whiteSpaced.rstrip())

# find
print(whiteSpaced.find("rd")) # index of rd
print(whiteSpaced.replace("W", "L"))
print("Lal" in myName) # Prints true/false
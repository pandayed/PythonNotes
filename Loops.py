# for loop
# we can iterate over anything that is iterable
for x in "Python":
    print(x)

for x in [10, 20, 30]:
    print(x)

# 0 to 4
for x in range(5):
    print(x)

# 2 to 9
for x in range(2, 10):
    print(x)

# 0 to 10 with step 2
for x in range(0, 10, 2):
    print(x)

# range function
print(range(5))
# range function returns range object
print(type(range(5)))
# directly printing list
print([1, 2, 3, 4, 5])


# break
names = ["lal", "vishal"]
for name in names:
    if name.startswith("l"):
        print("Found")
        break

# for else
# else comes after for and is executed if for does not break
for name in names:
    if(name.startswith("P")):
        print("Found")
else:
    print("Not found")
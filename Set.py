nums = [1, 1, 2, 3, 4, 5, 5]
uniqNums = set(nums)
print(uniqNums)
# set are in curly braces
secondSet = {1, 1, 2, 3}
print(secondSet)
secondSet.add(5)
secondSet.remove(5)

# union can be found using vertical bar
print(uniqNums | secondSet)

# intersection
print(uniqNums & secondSet)

# setA - setB
print(uniqNums - secondSet)

# symmatirc diff
print(uniqNums ^ secondSet)

# items are not in sequence in set so we cannot access them using index

if 1 in uniqNums:
    print("Present")
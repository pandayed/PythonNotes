# Unpacking Operator *
# in javascript we have spread operator i.e. ...(three dots) for the same
nums = [1, 2, 3]
# prints nums as a whole i.e. as a list
print(nums)

# with unpacking operator we get all the elements as individuals
print(*nums)

# we can unpack any iterable with unpacking operator
# both are same
nums = list(range(5))
print(nums)
nums = [*(range(5))]
print(nums)


# combining lists using unpacking operator
first = [1, 2]
second = [3, 4]
values = [*first, 5, 6, *second]
print(values)

# to unpack dictionaries we need two *
first = {"x":10}
second = {"y": 20, "z": 30, "x":40}
combined = {**first, **second}
# if two dics. have same key then last value will be used for the key
print(combined)
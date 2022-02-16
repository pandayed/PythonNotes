from array import  array

# arrays take less memory and work faster than list
# the memory and time diff is neglegilbe until data set is too big
# first parameter is typcode
myNos = array("i", [1, 2, 3])
print(myNos)
myNos.append(4)
myNos.insert(0, -1)
print(myNos)
myNos.pop()
print(myNos[0])
# every object/value in array must be of same type

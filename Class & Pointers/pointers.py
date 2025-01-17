# num1 = 11
# num2 = num1

# print('num1 = ', num1)
# print('num2 = ', num2)

# print('num1 is addressed to ', id(num1))
# print('num2 is addressed to ', id(num2))

# num2 = 22

# print('num1 = ', num1)
# print('num2 = ', num2)

# print('num1 is addressed to ', id(num1))
# print('num2 is addressed to ', id(num2))

#Integers are immutable, num1 can't be reassigned even if num1 & num2 are set equal 
#num1 & num2 point at the same place and we aren't able to change the value

# for dict
# dict1 = {'value': 11}

# dict2 = dict1

# print('dict1 = ', dict1)
# print('dict2 = ', dict2)

# print('dict1 is addressed to ', id(dict1))
# print('dict2 is addressed to ', id(dict2))

# dict2['value'] = 22

# print('dict1 = ', dict1)
# print('dict2 = ', dict2)

# print('dict1 is addressed to ', id(dict1))
# print('dict2 is addressed to ', id(dict2))

#Dictionaries are mutable, dict1 will be reassigned if dict1 & dict2 are set equal 
#dict1 & dict2 point at the same place and we are able to change the value

# for 3 dicts pointing at a new value
dict1 = {'value': 11}
dict3 = {'value':33}
dict2 = dict1 = dict3

print('dict1 = ', dict1)
print('dict2 = ', dict2)
print('dict = ', dict3)

print('dict1 is addressed to ', id(dict1))
print('dict2 is addressed to ', id(dict2))
print('dict3 is addressed to ', id(dict3))

dict2['value'] = 22

print('dict1 = ', dict1)
print('dict2 = ', dict2)
print('dict3 = ', dict3)

print('dict1 is addressed to ', id(dict1))
print('dict2 is addressed to ', id(dict2))
print('dict3 is addressed to ', id(dict3))

#the earlier values which do not have a head will be discarded by the program in the garbage collector
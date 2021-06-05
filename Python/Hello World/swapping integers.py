a = 1
b = 4

print(a, b)

# making a temporary variable
temp = a
a = b
b = temp

print(a, b)

# to make arithmetic look simple
c = a + b
a = c - a
b = c - a

print(a, b)

# using arithmetic
a = a + b
b = a - b
a = a - b

print(a, b)
"""can use * and / too but breaks at zero"""

# python comma operator
a, b = b, a

print(a, b)

# Swapping using xor
"""The bitwise XOR operator can be used to swap two variables. 
The XOR of two numbers x and y returns a number which has all the bits as 1 wherever bits of x and y differ. 
For example XOR of 10 (In Binary 1010) and 5 (In Binary 0101) is 1111 and XOR of 7 (0111) and 5 (0101) is (0010)"""
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

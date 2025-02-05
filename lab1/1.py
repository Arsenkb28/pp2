print("Topic - HOME")

print("Hello, Nikita!")

# ----------------------------------------

print("Topic - Syntax")

a = 69
b = 228
if a < b:
  print("Oh no")

# ----------------------------------------

print("Topic - Comments")

"""
I love comments
"""

# ----------------------------------------

print("Topic - Variables")

var1 = "Kanat"
var2 = str(442)
var3 = 442

print(var1, var2, var3)

# ----------------------------------------

print("Topic - Data Types")

print(type(1337))
print(type(1337.0))
print(type(133 + 7j))
print(type("1337"))
print(type([1, 3, 3, 7]))
print(type((1, 3, 3, 7)))
print(type({1, 3, 3, 7}))
print(type({1: 3, 3: 7}))

# ----------------------------------------

print("Topic - Numbers")

import random

num1 = 42
num2 = -6.9
num3 = 13 + 37j

print(num1 + num2, num1 - num3, num2 / num1, num3 / (num3 + num1))

print("You are lucky to have this nunmber -", random.randint(1, 1000000000))

# ----------------------------------------

print("Topic - Casting")

print(int(-1.999999999) + float(1.99999999) + complex(0))  # 0.99999999 + 0j
print(1000 + int("337"))

# ----------------------------------------

print("Topic - Strings")

str1 = "Nikita"
str2 = """
One man watched the city from a rooftop,
his cape billowing as thunder rumbled overhead.
He was - """
print(str2 + str1)
print("Topic - Boolean")

print(13 < 37)

a = 13
b = 37
if a < b:
  print(b)
else:
  print(a)

print(bool(False), bool(None), bool(0), bool(""), bool([]), bool(()), bool({}))  # Falsy values
print(bool(-2), bool("Hi"), bool([13, 37]))  # True values


class FalsyClass():
  def __len__(self):
    return 0


myobj = FalsyClass()
print(bool(myobj))

x = 200
print("x is instance of <class 'int'> class,", isinstance(x, int))

# ----------------------------------------

print("Topic - Operators")

a = 17
b = 3

print("a + b", a + b)
print("a - b", a - b)
print("a * b", a * b)
print("a ** b", a ** b)
print("a / b", a / b)
print("a // b", a // b)
print("a % b", a % b)
print("a & b", a & b)
print("a | b", a | b)
print("a ^ b", a ^ b)
print("~a, ~b", ~a, ~b)
print("a << b", a << b)
print("a >> b", a >> b)
print("a == b", a == b)
print("a != b", a != b)
print("a <= b", a <= b)
print("a < b", a < b)
print("a > b", a > b)
print("a >= b", a >= b)
print("a and b", a and b)
print("a or b", a or b)
print("not a, not b", not a, not b)

arr1 = [1, 3, 3, 7]
arr2 = [2, 2, 8]

print("b in arr1", b in arr1)
print("a not in arr1", a not in arr1)
print("arr1 is arr2", arr1 is arr2)
print("arr1 is not arr2", arr1 is not arr2)

casualty = 0
casualty += a
casualty -= a
casualty *= a
casualty /= a
casualty %= a
casualty //= a
casualty **= a

casualty = int(casualty)
casualty &= a
casualty |= a
casualty ^= a
casualty >>= a
casualty <<= a
1 + (casualty := a)

# ----------------------------------------

print("Topic - Lists")

your_list = ["Bulldozer", "Gazzele"]
my_list = ["Toyota", "BMW", "Mercedes"]

print(my_list, len(my_list), type(my_list), list((1, "2", ["Fiasko"])))

print(my_list[1])  # 'Toyota'
# print(my_list[133769])  # ERROR
print(my_list[-1])  # 'Mercedes'
print(my_list[1:])  # ['BMW', 'Mercedes']
print(my_list[1:-1])  # ['BMW']
print("BMW" in my_list[1:-1])  # True

my_list[0] = "Range Rover"  # ['Range Rover', 'BMW', 'Mercedes']
my_list[1:] = ["Modern BMW", "Modern Merdeces", "Tachka"]  #['Range Rover', 'Modern BMW', 'Modern Merdeces', 'Tachka']
my_list.insert(1, "Old BMW")  # ['Range Rover', 'Old BMW', 'Modern BMW', 'Modern Merdeces', 'Tachka']
my_list.append("Tesla")  # ['Range Rover', 'Old BMW', 'Modern BMW', 'Modern Merdeces', 'Tachka', 'Tesla']
my_list.pop()  # ['Range Rover', 'Old BMW', 'Modern BMW', 'Modern Merdeces', 'Tachka']
my_list.pop(-2)  # ['Range Rover', 'Old BMW', 'Modern BMW', 'Tachka']
my_list.remove("Old BMW")  # ['Range Rover', 'Modern BMW', 'Tachka']
# my_list.remove("Not existing car")  # ERROR
my_list.extend(["Boeing 737", "Vedro"])  # ['Range Rover', 'Modern BMW', 'Tachka', 'Boeing 737', 'Vedro']
del my_list[1]  # ['Range Rover', 'Tachka', 'Boeing 737', 'Vedro']
my_list.clear()  # []
# my_list.pop()  # ERROR

for val in your_list:
  print(val)  # 'Bulldozer' 'Gazzele'

for i in range(len(your_list)):
  print(your_list[i])  # 'Bulldozer' 'Gazzele'

my_list = ["Tachka lvl " + str(i) for i in range(1, 6) if i % 2 == 0]  # ['Tachka lvl 2', 'Tachka lvl 4']
my_list.sort(reverse=True)  # ['Tachka lvl 4', 'Tachka lvl 2']
my_list.reverse()  # ['Tachka lvl 2', 'Tachka lvl 4']

shallow_copy_list = my_list.copy()
shallow_copy_list = list(my_list)
shallow_copy_list = my_list[:]

my_list = my_list + shallow_copy_list * 2  # joining lists

# Other methods
print(my_list.count("Tachka lvl 4"))  # 3
print(my_list.index("Tachka lvl 4"))  # 1

# ----------------------------------------

print("Topic - Tuples")
t1 = (2, 2, "8")
t2 = tuple([13, 37])
print(t1, len(t1), type(t1))

print(t1 + t2 * 2)  # (2, 2, '8', 13, 37, 13, 37)

# t1[1:3] = t2  # WRONG, tuples are immutable
t1 = tuple(list(t1[:1]) + list(t2) + list(t1[3:]))  # (2, 13, 37)

a, *rest = t1  # a = 2, rest = [13, 37]

# Other methods
print(t1.count(13))  # 1
print(t1.index(13))  # 1

# ----------------------------------------

print("Topic - Sets")

empty_set = set()
s1 = {1, 3, 3, 3, "3", 7}
s2 = {2, 2, 8}

print(s1, len(s1), type(s1))

s1.add(9)  # {1, 3, '3', 7, 9}
s1.update(s2)  # {1, 2, 3, '3', 7, 8, 9}

# s1.remove(69) will raise an error
s1.remove(1)  # {2, 3, 7, 8, 9, '3'}
s1.discard(2)  # {3, 7, 8, 9, '3'}
s1.discard(2)  # {3, 7, 8, 9, '3'}

s1.clear()  # {}
del s1  # s1 now is not accessible
s1 = {4, 2}
list1 = [6, 9]

for val in s1:
  print(val)  # 2 4

print(s1 | s2, s1.union(s2))  # union does not mutate
print(s1.union(s2, list1))
# print(s1 | list1)  # ERROR

print(s1 & s2, s1.intersection(s2))
print(s1.intersection(s2, list1))
# print(s1 & list1)  # ERROR

s1.intersection_update(s2)  # s1 = {2}

print({0, 1} & {False, True})  # {False, True}

print(s1 - s2, s1.difference(s2))
print(s1.difference(s2, list1))
# print(s1 - list1)  # ERROR

s1.difference_update(s2)  # s1 = set()
s1 = {1, 2, 3}

print(s1 ^ s2, s1.symmetric_difference(s2))
print(s1.symmetric_difference(s2))
# print(s1 ^ list1, s1.symmetric_difference(s2, list1))  # ERROR

s1.difference_update(s2)  # s1 = set()
# other methods

s1 = {1, 3}
s2 = {1, 3, 7}

s1.copy()
s1.discard(3)
print(s1.isdisjoint(s2))
print(s2.issuperset(s1), s2 >= s1)
print(s1.issubset(s2), s1 <= s2)

# ----------------------------------------

print("Topic - Dictionaries")
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

dict1 = {
  "name": "Kanat",
  "course": 1,
  "age": 18,
}
dict2 = {}

print(dict1, len(dict1), type(dict1))

print(dict1["name"], dict1.get("name"))

keys, values, items = dict1.keys(), dict1.values(), dict1.items()
print(keys, values, items)
dict1["surname"] = "Kairat"  # added entry
print(keys, values, items)

print("surname" in dict1)

dict1.update({  # added a new entry and changed "name" value
  "name": "Tigrrr",
  "occupation": "Kaifovat'",
})

dict1.pop("age")  # removed entry with a key "age"
# dict1.pop("not existing key")  # ERROR

dict1.popitem()  # removed last inserted entry in python versions >= 3.7

del dict1["surname"]
# del dict1["not existing key"]  # ERROR

dict1.clear()

dict1 = {
  "name": "Kanat",
  "course": 1,
  "age": 18,
}

for key in dict1:
  print(key, dict1[key])
for key in dict1.keys():
  print(key)
for value in dict1.values():
  print(value)
for key, value in dict1.items():
  print(key, value)

# other methods
dict1.copy()
print(dict1.fromkeys([1, 2, 3], 1337))  # immutable method
print(dict1.setdefault("name", "Kanich"), dict1.setdefault("surname", "Kidalovich"))  # Kanat Kidalovich
print(dict1)

# other static methods
dict.fromkeys([1, 2, 3], 1337)


# ----------------------------------------

print("Topic - If...Else")

if True:
  if False:
    pass
  else:
    if False:
      pass
    elif True:
      print("HERE!")
    else:
      pass
else:
  pass

# ----------------------------------------

print("Topic - While loops")

i = 0
while (i := i + 1) - 1 < 10:
  if i & 1:
    continue
  print(i)  # 2 4 6 8 10

# ----------------------------------------

print("Topic - For loops")
for i in range(0, 101, 3):
  if i % 4 == 0 or i % 5 == 0 or i % 7 == 0:
    continue
  if i * 4 % 228 == 0:
    print(f"Oh no {i} came here!")  # Oh no 57 came here!
    break
  print(i)  # 3 6 9 18 27 33 39 51 54
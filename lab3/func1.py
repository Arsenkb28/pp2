def gram_to_ounce(x):
    return 28.3495231 * x

gram = int(input())
ounce = gram_to_ounce(gram)

print(ounce)
#2
def celcius(F):
    return 5/9 * (F-32)
print(celcius(int(input())))
#3
""" 
    r + c = 35     (1 1 | 35)               (1  1 | 35)                (1 1 | 35)              (1 0 | 12)
    4r + 2c = 94   (4 2 | 94)  R2->-4R1+R2  (0 -2 |-46)  R2->-(1/2)R2  (0 1 | 23)  R1->-R2+R1  (0 1 | 23) 

    (r) = (12)
    (c) = (35)

    by formula: c = -(numleg-4*numhead)/2,  r = numhead-c
"""

def solve(numheads, numlegs):
    c = -(numlegs-4*numheads)/2
    r = numheads-c
    return r, c

print(solve(35, 94))
#4
def filter_prime(l):
    nwl = []
    for i in l:
        if i < 1:
            continue
        check = True
        for j in range(2, int(pow(i, 1/2))+1):
            if i%j == 0:
                check = False
                break
        if check:
            nwl.append(i)
    return nwl
#You are given list of numbers separated by spaces
arr = list(map(int, input().split()))

print(filter_prime(arr))
#5
from itertools import permutations

def perm(s):
    return list(permutations(s))


a = perm('abc')
for i in a:
    print(i)





# out=[]
# def perm(msg, i, length):
#     if i==length:
#         out.append("".join(msg))
#     else:
#         for j in range(i, length):
#             msg[i], msg[j] = msg[j], msg[i]
#             perm(msg, i+1, length)
#             msg[j], msg[i] = msg[i], msg[j]

# msg="acb"
# perm(list(msg), 0, len(msg))
# print(out)
#6
def reversed(s = input()):
    return s[::-1]

s = reversed()
print(s)
#7
def has_33(nums):
    d = [i for i, el in enumerate(nums) if el==3]
    for i in range(len(d)-1):
        if d[i+1]-d[i] == 1:
            return True
    return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])

# print(has_33([1, 3, 3]))
# print(has_33([1, 3, 1, 3]))
# print(has_33([3, 1, 3]))
#8
def spy_game(nums):
    id = -1
    while True:
        try:
            id = nums.index(7, id+1)
            if nums[:id].count(0) >= 2:
                return True
        except:
            #return False
            break
    return False

spy_game([1,2,4,0,0,7,5]) #True
spy_game([1,0,2,4,0,5,7]) #True
spy_game([1,7,2,0,4,5,0]) #False


print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False
#9
import math
def v(r):
    return 4/3 * math.pi * pow(r, 3)

if __name__ == "__main__":
    r = int(input())
    print(f'Volume = {v(r)}')
#10
def unique(l):
    d = []
    for i in l:
        if i not in d: 
            d.append(i)
    return d
if __name__ == "__main__":
    l = list(map(int, input().split()))

    new = unique(l)

    print(new)

#11
def palindrome(s):
    return s[::-1] == s

if __name__ == "__main__":
    s = input()
    print(palindrome(s))
#12
def histogram(l):
    for i in l:
        print('*'*i)

histogram([4, 9, 7])
#13
import random
def guess(num, i = 0):
    print('Take a guess.')
    n = int(input())
    if n < num:
        print('\nYour guess is too low.')
        return guess(num, i+1)
    elif n > num:
        print('\nYour guess is too high.')
        return guess(num, i+1)
    else:
        return i+1
    
if __name__ == "__main__":
    num = random.randint(1, 20)
    name = input('Hello! What is your name?\n')
    print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')

    attempts = guess(num)
    print(f'\nGood job, {name}! You guessed my number in {attempts} guesses!')
#14
def calc_sphere_volume(radius):
  return (4 * radius ** 3 * math.pi) / 3


def uniq(arr1):
  arr = sorted(arr1)
  res = []
  for i in range(len(arr) - 1):
    if arr[i] != arr[i + 1]:
      res.append(arr[i])
  res.append(arr[-1])
  return res


def is_palindrome(s):
  s = "".join(s.split(" ")).lower()
  return s == s[::-1]


def histogram(nums):
  for num in nums:
    print("*" * num)

def game():
  start, end = 1, 20
  user_attempts = 0
  name = ""
  
  print("Hello! What is your name?")
  name = input()
  
  print()
  print(f"Well, {name}, I am thinking of a number between {start} and {end}.")
  guessed_num = random.randint(start, end)

  while 1:
    print("Take a guess.")
    user_num = int(input())
    user_attempts += 1
    
    print()
    if user_num < guessed_num:
      print("Your guess is too low.")
    elif user_num > guessed_num:
      print("Your guess is too high.")
    else:
      print(f"Good job, {name}! You guessed my number in {user_attempts} guesses!")
      break



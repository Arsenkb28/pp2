import datetime


def subtract_date(date = datetime.datetime.now(), days=5):  # takes now instance
  return date - datetime.timedelta(days=days)


def print_sibling_days(date = datetime.datetime.now()):
  print("Yesterday:", (date - datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))
  print("Today:", date.strftime("%A, %d %B %Y, %H:%M:%S"))
  print("Tomorrow:", (date + datetime.timedelta(days=1)).strftime("%A, %d %B %Y, %H:%M:%S"))


def drop_ms(date):
  return date.replace(microsecond=0)


def seconds_diff(date1, date2):
  return round((abs(date1 - date2)).total_seconds())


if __name__ == "__main__":
  now = datetime.datetime.now()
  print(now)
  print(subtract_date(now))

  print_sibling_days(now)

  print(drop_ms(now))
  # print(second_diff(now, datetime.datetime.combine(datetime.date(2023, 1, 1), datetime.datetime.now().time())))
  # print(second_diff(now, datetime.datetime.combine(datetime.date(2025, 1, 22), datetime.datetime.now().time())))




#generator
def sqaure_numbers(upper_bound):
  upper_bound = max(1, upper_bound)

  it = 1
  while it <= upper_bound:
    yield it ** 2
    it += 1


def even_numbers(upper_bound):
  upper_bound = max(0, upper_bound)

  it = 0
  while it <= upper_bound:
    if it % 2 == 0:
      yield it
    it += 1


def magic_numbers(upper_bound):
  upper_bound = max(0, upper_bound)

  it = 0
  while it <= upper_bound:
    if it % 3 == 0 and it % 4 == 0:
      yield it
    it += 1


def range_square(lower_bound, upper_bound):
  upper_bound = max(lower_bound, upper_bound)

  it = lower_bound
  while it <= upper_bound:
    yield it ** 2
    it += 1


def decrease_numbers(upper_bound, lower_bound = 0):
  upper_bound = max(lower_bound, upper_bound)

  it = upper_bound
  while it >= lower_bound:
    yield it
    it -= 1


if __name__ == "__main__":
  print(*even_numbers(int(input())), sep=", ")
  # print(*magic_numbers(int(input())), sep=", ")
  # print(*range_square(*map(int, input().split())), sep=", ")
  print(*decrease_numbers(*map(int, input().split())), sep=", ")

#json
import json

file = open("Lab 04/sample-data.json", "r")
data = file.read()
parsed = json.loads(data)

# print(parsed)

imdata = parsed["imdata"]

def is_valid_record(record):
  try:
    attr = record["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    ethNum = int(dn[dn.rfind("/") + 1:dn.rfind("]")])
    return 33 <= ethNum <= 35
  except:
    return False


interface_len = 80
dn_pad = 50
descr_pad = 20
speed_pad = 6
mtu_pad = 5

dn_key = "dn"
descr_key = "descr"
speed_key = "speed"
mtu_key = "mtu"

dn_header = "DN"
descr_header = "Description"
speed_header = "Speed"
mtu_header = "MTU"

print("Interface Status")
print("=" * interface_len)

print(
  dn_header.ljust(dn_pad),
  descr_header.ljust(descr_pad),
  speed_header.ljust(speed_pad),
  mtu_header.ljust(mtu_pad)
)
print(
  "-" * dn_pad,
  "-" * descr_pad,
  "-" * speed_pad,
  "-" * mtu_pad
)

for record in imdata:
  if not is_valid_record(record):
    continue
  
  attr = record["l1PhysIf"]["attributes"]

  print(
    attr[dn_key].ljust(dn_pad),
    attr[descr_key].ljust(descr_pad),
    attr[speed_key].ljust(speed_pad),
    attr[mtu_key].ljust(mtu_pad)
  )
#math

import math

def convert_to_rad(degree):
  return degree / 180 * math.pi


def calc_trapezoid_area(height, base1, base2):
  return height * (base1 + base2) / 2;


def calc_reg_polython_area(sides, side_len):
  apophem =  side_len / (2 * math.tan(convert_to_rad(180 / sides)))
  return round(sides * side_len * apophem / 2, 5)


def calc_parallelogram_area(base, height):
  return base * height;


print(calc_trapezoid_area(5, 5, 6))
print(calc_reg_polython_area(4, 25))
print(calc_parallelogram_area(5, 6))

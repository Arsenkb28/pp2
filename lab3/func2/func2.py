import functools
from payload import movies

def check(name = "Love"):
    l = [i["imdb"] for i in movies if i["name"]==name]
    return l[0] > 5.5

print(check())
from payload import movies
def sublist_above_5p5():
    l = [i["name"] for i in movies if i["imdb"] > 5.5]
    return l

# print(sublist_above_5p5())



from payload import movies
def average_imdb(l):
    d = [i["imdb"] for i in movies if i["name"] in l]
    return sum(d)/len(l)

# print(average_imdb(["Bride Wars", "Love", "Colonia", "The Help", "Usual Suspects"]))

from payload import movies

def category_imdb(category):
    l = [i["imdb"] for i in movies if i["category"] == category]
    return sum(l)/len(l)

# print(category_imdb('Crime')) #4.0
# print(category_imdb('Romance')) #6.7
# print(category_imdb('Thriller')) #5.6
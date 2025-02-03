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
def categories(category = "Romance"):
    l = [i['name'] for i in movies if i['category']==category]
    return l

# print(categories())
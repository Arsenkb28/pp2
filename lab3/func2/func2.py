import functools
from payload import movies

def check(name = "Love"):
    l = [i["imdb"] for i in movies if i["name"]==name]
    return l[0] > 5.5

print(check())


def calc_avg_imbd(movies, filter_func=None):
  total = 0
  if filter_func is not None:
    movies = filter_func(movies)
  for movie in movies:
    total += float(movie["imdb"])
  return total / len(movies)



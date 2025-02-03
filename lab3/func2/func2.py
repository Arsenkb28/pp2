import functools
from payload import movies

def is_above(movie, score = 5.5):
  return movie["imdb"] > score


def filter_movies(movies, score = None, category=None):
  res = []
  for movie in movies:
    if score is not None and not is_above(movie, score):
      continue
    if category is not None and movie["category"].lower() != category.lower():
      continue
    res.append(movie)
  return res


def calc_avg_imbd(movies, filter_func=None):
  total = 0
  if filter_func is not None:
    movies = filter_func(movies)
  for movie in movies:
    total += float(movie["imdb"])
  return total / len(movies)



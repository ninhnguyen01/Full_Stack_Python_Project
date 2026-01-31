from functools import lru_cache
from timeit import timeit

billion = 1_000_000_000

@lru_cache
def sum_thing(number):
    return sum(range(number))

print(timeit("sum_thing(billion)", globals=globals(), number=1))

print(timeit("sum_thing(billion)", globals=globals(), number=1))

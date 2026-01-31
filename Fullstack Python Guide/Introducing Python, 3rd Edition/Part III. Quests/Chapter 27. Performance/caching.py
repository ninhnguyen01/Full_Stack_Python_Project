from functools import cache
from timeit import timeit

fast_sum = cache(sum)
billion = 1_000_000_000

print(timeit("fast_sum(range(billion))", globals=globals(), number=1))

print(timeit("fast_sum(range(billion))", globals=globals(), number=1))

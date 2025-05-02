import time
from collections import OrderedDict
from functools import wraps


def lru(max_size: int = 128):
    def cache(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(*args) + str(**kwargs)

            if key in cache:
                cache.move_to_end(key)
                print(f"Cache hit {key}, {cache[key]}")
                return cache[key]

            res = func(*args, **kwargs)
            cache[key] = res
            print(f"Cache miss {key}, {cache[key]}")

            if len(cache) > max_size:
                print(f"Max size cache reached, removing last item of the {cache}")
                cache.popitem(last=False)
                print(f"New cache: {cache}")

            return cache[key]

        return wrapper

    return cache


if __name__ == "__main__":

    @lru(max_size=3)
    def expensive_computations(n: int):
        time.sleep(n)
        return

    expensive_computations(3)
    expensive_computations(2)
    expensive_computations(1)
    expensive_computations(4)
    expensive_computations(4)
    expensive_computations(4)

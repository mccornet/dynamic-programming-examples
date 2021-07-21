"""
Naive Recursive Fibonacci Function
"""
def fibonacci(n):
    if n <= 2 : return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

"""
Using Functools to cache the result and reduce the speed to O(n)
"""
from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n <= 2 : return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


"""
Using the bottom up approach to reduce call stack overhead
"""
def fibonacci(n):
    prev = curr = 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    return curr


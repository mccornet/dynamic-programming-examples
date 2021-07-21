# Dynamic Programming Examples

This is a summary of textbook examples about dynamic programming.

# The Fibonacci sequence

> **Based on**:
>
> Programming Interview Problems: Dynamic Programming, Leonardo Rossi, Chapter 3

The Fibonacci sequence is the default example of dynamic programming in action. Dynamic programming is recursive programming with memoization. A recursive version without a cache is given by:

```python
def fibonacci(n):
    if n <= 2 : return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

This results in a lot of redundant calls and runs in $O(2^n)$ time.



The python library offers easy caching with functools lru_cache

```python
from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n <= 2 : return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

## Dynamic programming, bottom-up

A more efficient implementation (but often less intuitive for most) is to use the bottom up approach instead. Only the last two numbers are needed to calculate the next number if the result is built from the bottom up instead.

```python
def fibonacci(n):
    prev = curr = 1
    for _ in range(n - 2):
        prev, curr = curr, prev + curr
    
    return curr
```



# Optimal stock market strategy

# Change making

# Number of expressions with a target result

# The maximum-sum subarray - Kadane’s algorithm

> **Based on**:
>
> Programming Interview Problems: Dynamic Programming, Leonardo Rossi, Chapter 8
>
> **Related leetcode.com**
>
> [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

Given an array of integers, find the contiguous subarray having the largest sum. Return its sum.

> **Example**
>
> For [1, 1, 2, 3, 2], the sum is 6 for the subarray [1, 2, 3].

## Solution

**Observation 1** It can make sense to include negative numbers in the solution. 

![](https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p8_1.png)

**Observation 2** It is possible to create a running sum over an array.

![](https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p8_2.png)

**Summary**

- To find the maximum-sum subarray, examine smaller chunks of the array.
- A bigger chunk can be formed by appending an item to the chunk preceding it; this should be done only when the sum of the preceding chunk is positive;
- When the sum of the preceding chunk is negative, start a new chunk containing a single element.
- The maximum-sum subarray is the chunk with the largest sum.

## Kadane's algorithm *O*(n) time, *O*(1) space

Instead of keeping all computed chunks, compute a running maximum instead. Only keep track of the best chunk ever seen.

```python
def find_max_sum_subarray(array: list[int]) -> int:
    # edge case
    if not array: return 0

    prev_chunk = -float('inf')
    best_chunk = -float('inf')

    for num in array:
        if prev_chunk < 0:
            chunk = num
        else:
            chunk = prev_chunk + num

        # update the running maximum
        best_chunk = max(best_chunk, chunk)
        # Record the array chunk
        prev_chunk = chunk

    return best_chunk
```

It is possible to improve this algorithm's speed even more.

## Improvement 1
- It is possible to set the initial values to the first value of the array


```python
def find_max_sum_subarray(self, nums: list[int]) -> int:
    if not nums: return 0

    best_chunk = prev_chunk = nums[0]  # initialize with the first value

    for num in nums[1:]:
        # reset if we go below zero.
        if prev_chunk < 0 : prev_chunk = 0
        prev_chunk = prev_chunk + num
        
        # Update the running maximum        
        if best_chunk < prev_chunk: best_chunk = prev_chunk

    return best_chunk
```

## Improvement 2

> Inspired by leetcode.com problem 53

It is not needed to check if the previous chunk became negative; if the max value between the current chunk + the next number and the next number is taken. See the second array for this example. After adding the -4 the next iteration the number 1 will be a bigger value than -1.

> **Note**
>
> This max call simplified the code, but made it harder to understand. It is not always worth sacrificing speed over readability.

```python
def find_max_sum_subarray(self, nums: list[int]) -> int:
    if not nums: return 0

    best_chunk = curr_chunk = nums[0]  

    for num in nums[1:]:
        # Keep adding numbers. Once a chunk becomes negative
        # The next positive number will start a new chunk
        curr_chunk = max(curr_chunk + num, num)
        # Update the running maximum
        if best_chunk < curr_chunk: best_chunk = curr_chunk

    return best_chunk
```



# The maximum-product subarray

Given an array of integers, return the product of the contiguous subarray having the largest product.

> **Examples**
>
> - for [2, 3, 4], the product is 24 for the subarray [2, 3, 4].
> - for [-2, 3, 4], the product is 12 for the subarray [3, 4].
> - for [-2, 3, -4], the product is 24 for the subarray [-2, 3, -4].





# Largest Rectangle in skyline

> **Based on**:
>
> Programming Interview Problems: Dynamic Programming, Leonardo Rossi, Chapter 22

Given a skyline where all buildings are rectangular and have the same width. The skyline is encoded as an array of heights. Return the area of the largest rectangle in the skyline that is covered by buildings.

> **Example**
>
> skyline = [1, 3, 5, 4, 2, 5, 1]. 
> The largest rectangle has area 10
>
> Formed by 3, 5, 4, 2, 5, 5
> 5 buildings limited by height 2
>
> <img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_1.png" alt="Problem Example" style="zoom:67%;" />

## Solution

Notice the following properties:
- Any time the height increases there is a potentially taller rectangle.
- Any time the height decreases, taller buildings from the left cannot contribute to the current rectangle, so their upper parts can be ignored.


Based on this it is possible to formulate the following solution:
- Iterate with the right pointer over the skyline.
- Every time the height increases, grow a list of candidate left pointers.    
- When the height decreases, trim the left candidates and update the area.

<img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_2.png" alt="Problem Example" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_3.png" alt="Problem Example" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_4.png" alt="Problem Example" style="zoom:67%;" />

<img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_5.png" alt="Problem Example" style="zoom:67%;" />


```python
from collections import namedtuple


def find_largest_rectangle(skyline):
    # Pad the skyline with zero, to avoid having to clean up
    # left_candidates at the end of the iteration.
    skyline = skyline + [0]
    num_buildings = len(skyline)

    # store each candidate as a named tuple with fields index and height. 
    # As the right pointer advances, remove left candidates taller 
    # than the current building. Keep track of the last trimmed pointer 
    # to allow the trimmed buildings with a shorter candidate
    Candidate = namedtuple('Candidate', ['index', 'height'])
    left_candidates = []
    largest_area = 0

    for right in range(num_buildings):
        height = skyline[right]

        # Left pointer of the next candidate to be created.
        next_left = right
        while left_candidates and left_candidates[-1].height >= height:
            # Update area.
            # We remove the rectangle starting at left and ending
            # at right-1. It has height left_candidates[-1].height.
            left = left_candidates[-1].index
            width = right - left
            area = width * left_candidates[-1].height
            largest_area = max(largest_area, area)
            # Possible next candidate by trimming down the building.
            next_left = left
            del left_candidates[-1]

        left_candidates.append(Candidate(index=next_left, height=height))

    return largest_area
```
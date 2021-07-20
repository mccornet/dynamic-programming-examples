#Dynamic Programming Examples

This is a summary of textbook examples about dynamic programming.


#Problems

- The Fibonacci sequence
- Optimal stock market strategy
- Change-making
- Number of expressions with a target result (Kadane’s algorithm)
- Largest rectangle in skyline


# The Fibonacci sequence

# Optimal stock market strategy

# Change making

# Number of expressions with a target result

# The maximum-sum subarray - Kadane’s algorithm

Given an array of integers, find the contiguous subarray having the largest sum. Return its sum.

## Example
For [1, 1, 2, 3, 2], the sum is 6 for the subarray [1, 2, 3].

## Solution 1:


#The maximum-product subarray

Given an array of integers, return the product of the contiguous subarray having the largest product.

## Examples

- for [2, 3, 4], the product is 24 for the subarray [2, 3, 4].
- for [-2, 3, 4], the product is 12 for the subarray [3, 4].
- for [-2, 3, -4], the product is 24 for the subarray [-2, 3, -4].





#Largest Rectangle in skyline

Source: "Programming Interview Problems: Dynamic Programming, Leonardo Rossi"

Given a skyline where all buildings are rectangular and have the same width. The skyline is encoded as an array of heights. Return the area of the largest rectangle in the skyline that is covered by buildings.

## Example

skyline = [1, 3, 5, 4, 2, 5, 1]. 
The largest rectangle has area 10

Formed by 3, 5, 4, 2, 5, 5
5 buildings limited by height 2

<img src="https://raw.githubusercontent.com/mccornet/dynamic-programming-examples/main/images/rossi_p22_1.png" alt="Problem Example" style="zoom:67%;" />

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
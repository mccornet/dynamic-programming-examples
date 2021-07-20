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


if __name__ == '__main__':
    t1 = [1, 3, 5, 4, 2, 5, 1]
    a1 = 10

    assert find_largest_rectangle(t1) == 10
    print("Tests passed")

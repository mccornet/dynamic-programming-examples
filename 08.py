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


def find_max_sum_subarray(self, nums: list[int]) -> int:
    if not nums: return 0

    best_chunk = curr_chunk = nums[0]  # initialize with the first value

    for num in nums[1:]:
        # Once a chunk becomes negative
        # The next number will automatically start a new chunk
        curr_chunk = max(curr_chunk + num, num)
        
        # Record the running maximum
        if best_chunk < curr_chunk: best_chunk = curr_chunk

    return best_chunk



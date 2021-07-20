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

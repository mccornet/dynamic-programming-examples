def find_max_sum_subarray(array):
    # edge case
    if not array: return 0

    prev_chunk = -float('inf')
    best_chunk = -float('inf')

    for item in array:
        if prev_chunk < 0:
            chunk = item
        else:
            chunk = prev_chunk + item

        # update the running maximum
        best_chunk = max(best_chunk, chunk)
        # Record the array chunk
        prev_chunk = chunk

    return best_chunk

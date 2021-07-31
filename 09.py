def maxProductSubarray(array):

    def chunkGenerator(array):
        chunk = []
        # a zero to simplify elif to yield the last value
        for value in array + [0]:  
            if value: 
                chunk.append(value)
            elif chunk:
                yield chunk
                chunk = []  # dont forget to clean the chunk

    def twoPassMax(chunk):

        def productPass(chunk):
            best, curr = -float('inf'), 1
            for value in chunk:
                curr *= value
                if best < curr: best = curr
            return best
        
        return max(productPass(chunk), productPass(chunk[::-1]))

    # Calculate the max product of the whole array
    # By storing the biggest value seen
    best = -float('inf')
    for chunk in chunkGenerator(array):
        curr = twoPassMax(chunk)
        if best < curr: best = curr
    
    return best



def maxProductSubarray(array):

    def productPass(array):
        best, curr = 0, 1
        for value in array:   
            curr *= value
            # Reset the value if a zero was encountered
            if not curr: curr = value
     
            if best < curr: best = curr
        return best
        
    return max(productPass(array), productPass(array[::-1]))


"""
Single pass solution
"""
def maxProductSubarray(array):
    max_chunk = -float('inf')
    min_chunk = float('inf')
    global_max = -float('inf')

    for value in array:
        # Compute candidates for the max-product subarray
        # ending with the current element:
        # Candidate 1: Start a new subarray
        max_new_chunk = value
        # Candidate 2: continue positive subarray
        if max_chunk > 0 and value > 0:
            max_continue_positive = max_chunk * value
        else:
            max_continue_positive = -float('inf')
        # Candidate 3: flip sign of negative subarray
        if min_chunk < 0 and value < 0:
            max_flip_negative = min_chunk * value
        else:
            max_flip_negative = -float('inf')
        
        # Compute candidates for the min-product subarray
        # ending with the current element
        # Candidate 1: start a new subarray
        min_new_chunk = value
        # Candidate 2: continue negative subarray
        if min_chunk < 0 and value > 0:
            min_continue_negative = min_chunk * value
        else:
            min_continue_negative = float('inf')
        # Candidate 3: flip sign of positive subarray
        if max_chunk > 0 and value < 0:
            min_flip_positive = max_chunk * value
        else:
            min_flip_positive = float('inf')

        # Choose the best Candidate
        max_chunk = max(max_new_chunk, max_continue_positive, max_flip_negative)
        min_chunk = max(min_new_chunk, min_continue_negative, min_flip_positive)

        # update global max
        if global_max < max_chunk: global_max = max_chunk
    
    return global_max


print(maxProductSubarray([2, 3, -4]))
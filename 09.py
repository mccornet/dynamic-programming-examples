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
            best, curr = 0, 1
            for value in chunk:
                curr *= value
                if best < curr: best = curr
            return best
        
        return max(productPass(chunk), productPass(chunk[::-1]))

    # Calculate the max product of the whole array
    # By storing the biggest value seen
    best = 0
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


print(maxProductSubarray([2, 3, -4]))
'''
Array Pair Sum
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS


'''


def store_results(arr,k):
    # temp
    s = set()
    out = set()
    for item in arr:
        diff = k-item
        
        if diff not in s:
            s.add(item)
        else:
            out.add((min(item,diff), max(item,diff)))
    return out
    
print(store_results([1,3,2,2],4))
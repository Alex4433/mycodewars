def max_sequence(arr):
    result = 0
    for element in range(len(arr)):
        max_in = arr[element]
        for element_inner in range(element + 1, len(arr)):
            max_in += arr[element_inner]
            result = max_in if max_in > result else result
    return result


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

'''
5 kyu
Maximum subarray sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def snail(snail_map):
    len_array = len(snail_map)
    result = []

    for i in range(len_array):
        result.append(snail_map[0][i])

    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

a = [[1, 2],
     [3, 4]]

print(snail(array))
print(snail(a))

'''
4 kyu
Snail
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

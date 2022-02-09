def snail(snail_map):
    result = []
    while len(snail_map) >= 0:
        try:
            for key in snail_map[0]:  # get top row
                result.append(key)
            snail_map.pop(0)
            for key in range(len(snail_map)):  # get right column
                result.append(snail_map[key][-1])
                snail_map[key].pop(-1)
            for key in range(len(snail_map) - 1, -1, -1):  # get bottom column
                result.append(snail_map[-1][key])
            snail_map.pop(-1)
            for key in range(len(snail_map) - 1, -1, -1):  # get left column
                result.append(snail_map[key][0])
                snail_map[key].pop(0)
        except:
            return result
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

# [1,2,3,6,9,8,7,4,5]


a = [[1, 2],
     [3, 4]]

print(snail(array))

[1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 6, 11, 16, 7, 8, 9, 14, 19, 18, 17, 12, 13]
[1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13]

matrix = [[1, 4, 11, 3, 6],
          [6, 9, 5, 6, 6],
          [6, 5, 2, 9, 10],
          [11, 6, 4, 4, 7],
          [10, 5, 2, 6, 5]]
print(matrix)

print(snail(matrix))

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

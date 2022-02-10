def move_zeros(array):
    for i in range(array.count(0)):
        array.remove(0)
        array.append(0)
    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

'''
5 kyu
Moving Zeros To
The End

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

'''

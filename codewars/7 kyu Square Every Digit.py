def square_digits(num):
    res = ''
    for i in str(num):
        res += str(int(i) ** 2)
    return res


print(square_digits(9119))

'''
Square Every Digit 7 KUA

Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
'''

def digital_root(n):
    if len(str(n)) == 1:
        return n
    return digital_root(sum(list(map(int, list(str(n))))))


print(digital_root(493193))

'''
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples
'''

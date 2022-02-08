def remove(s):
    repeat = 0
    for i in s:
        if i == '!':
            repeat += 1
    if repeat == 1 and s[-1] == '!':
        return s
    res = ''
    for i in s:
        if i != '!':
            res += i
    res += '!'
    return res


print(remove('!Hi'))

'''
Description:

Remove all exclamation marks from sentence but ensure a exclamation mark at the end of string. For a beginner kata, you can assume that the input data is always a non empty string, no need to verify it.
Examples

remove("Hi!") === "Hi!"
remove("Hi!!!") === "Hi!"
remove("!Hi") === "Hi!"
remove("!Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!"
remove("Hi") === "Hi!"

'''

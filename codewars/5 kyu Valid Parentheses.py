def valid_parentheses(string):
    open_par = 0
    close_par = 0
    for let in string:
        if let == ')':
            close_par += 1
        if let == '(':
            open_par += 1
        if close_par > open_par:
            return False
    return True if close_par == open_par else False


print(valid_parentheses("hi())("))

'''

5 kyu
Valid Parentheses

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''

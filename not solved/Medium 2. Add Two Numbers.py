# TypeError: object of type 'ListNode' has no len()
#     if len(l1) < len(l2):
# Line 10 in addTwoNumbers (Solution.py)
#     ret = Solution().addTwoNumbers(param_1, param_2)
# Line 53 in _driver (Solution.py)
#     _driver()
# Line 64 in <module> (Solution.py)


class Solution:
    def addTwoNumbers(self, l1, l2):
        res = []
        mood = 0
        if len(l1) < len(l2):
            l1, l2 = l2, l1
        if len(l1) == len(l2):
            l1 = l1[::-1]
        for i in range(len(l1)):
            # i = 0 - i
            try:
                l1[i] = l1[i] + l2[i] + mood
            except:
                l1[i] += mood
            if l1[i] >= 10:
                if i == len(l1) - 1:
                    l1.append(mood)
                mood = 1
                l1[i] = l1[i] % 10
            else:
                mood = 0
        return l1


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
#  = [8,9,9,9,0,0,0,1]


print(Solution.addTwoNumbers(1, l1, l2))

'''

2. Add Two Numbers
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]



Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

'''

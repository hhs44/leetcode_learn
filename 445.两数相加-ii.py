     #
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        node = None
        carry = 0
        while stack1 or stack2 :
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            
            s1 = x + y + carry
            carry = s1 // 10
            s2 = s1 % 10
            temp = ListNode(s2)
            temp.next = node
            node = temp
        if carry != 0:
            res = ListNode(carry)
            res.next = temp
            return res

        return node
# @lc code=end


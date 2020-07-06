#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = ''
        stack2 = ''

        while l1:
            stack1 = str(l1.val) + stack1
            l1 = l1.next
        while l2:
            stack2 = str(l2.val) + stack2
            l2 = l2.next
        res = int(stack1) + int(stack2)
        node = None
        for x in str(res):
            temp = ListNode(int(x))
            temp.next = node
            node = temp

        return node





# @lc code=end

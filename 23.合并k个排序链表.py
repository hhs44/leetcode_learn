#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue()
        node = None
        t = 0
        for i in lists:
            pq.put((i.val, t, i))
            t +=1
        while pq:
            if node is None:
                node = pq.get()[2]
                pq.put((node.next.val, t, node.next))
                t += 1
            else:
                temp = pq.get()[2]
                node.next = temp
                if temp.next == None:
                    pass
                else:
                    pq.put((temp.next.val, t, temp.next))
                    t += 1
        return node
            
            
# @lc code=end


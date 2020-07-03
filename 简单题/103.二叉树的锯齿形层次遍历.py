#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [(root,)]
        res = []
        step = 1
        while nodes:
            res.append([x.val for n in nodes[::step] for x in n[::step] if x ])
            step = -step
            nodes = [(x.left, x.right) for n in nodes for x in n if x] 
        return res[:-1]   
            
# @lc code=end


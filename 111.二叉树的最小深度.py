#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        res = 0
        if not root.left and not root.right:
            res = 1
        elif root.left and root.right:
            res = min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left:
            res = self.minDepth(root.left) + 1
        else:
            res = self.minDepth(root.right) + 1
        return res
            
        
# @lc code=end


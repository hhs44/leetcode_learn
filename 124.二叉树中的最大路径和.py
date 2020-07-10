'''
@Author: your name
@Date: 2020-07-10 10:37:19
@LastEditTime: 2020-07-10 10:54:22
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode-learn\124.二叉树中的最大路径和.py
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        def oneside(root):
            if not root :return 0
            left = oneside(root.left)
            right = oneside(root.right)
            self.ans = max(self.ans, left + right + root.val)
            return max(0, max(left, right) + root.val)
        oneside(root)
        return self.ans
# @lc code=end


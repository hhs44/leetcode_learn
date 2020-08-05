#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(root):
            if not root:return [0,0]
            left = helper(root.left)
            right = helper(root.right)
            robValue = left[1] + right[1] + root.val
            skipValue = max(left[0], left[1]) + max(right[0], right[1])
            return [robValue, skipValue]
        a = helper(root)
        return max(a[0], a[1])
# @lc code=end


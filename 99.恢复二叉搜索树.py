#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        Trees = lambda x:[] if not x else Trees(x.left) + [x] + Trees(x.right)
        a = Trees(root)
        sa = sorted(a, key=lambda x:x.val)
        temp = [a[i] for i in range(len(a)) if a[i] != sa[i]]
        temp[0].val, temp[1].val = temp[1].val, temp[0].val
# @lc code=end


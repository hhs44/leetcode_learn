#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def gen(num):
            if not num: yield None
            for i, n in enumerate(num):
                for l in gen(num[:i]):
                    for r in gen(num[i + 1:]):
                        yield TreeNode(n,l,r)
        return bool(n) * [*gen([*range(1, 1 + n)])]
                     
# @lc code=end


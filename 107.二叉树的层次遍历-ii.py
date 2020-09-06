#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res)<depth+1:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        return res[::-1]

# @lc code=end


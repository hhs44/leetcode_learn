#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue = ll
        return res
# @lc code=end


#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # if not root :return False
        # if not root.left and not root.right:
        #     return sum == root.val
        # return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
        if not root:
            return False
        que_node = collections.deque([root])
        que_val = collections.deque([root.val])
        while que_node:
            now = que_node.popleft()
            temp = que_val.popleft()
            if not now.left and not now.right:
                if temp == sum:
                    return True
                continue
            if now.left:
                que_node.append(now.left)
                que_val.append(now.left.val + temp)
            if now.right:
                que_node.append(now.right)
                que_val.append(now.right.val + temp)
        return False

        
# @lc code=end


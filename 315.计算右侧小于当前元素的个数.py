#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        root, n = None, len(nums)
        res = [0 for _ in range(n)]
        for i in reversed(range(n)):
            root = self.insertNode(root, nums[i], res, i)
        return res
    
    
    def insertNode(self, root, val, res, res_index):
        if root == None:
            root = TreeNode(val)
        elif val <= root.val:
            root.count += 1
            root.left = self.insertNode(root.left, val, res, res_index)
        elif val > root.val:
            res[res_index] += root.count + 1
            root.right = self.insertNode(root.right,val,res,res_index)
        return root
# @lc code=end


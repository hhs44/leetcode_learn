#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)   
# @lc code=end


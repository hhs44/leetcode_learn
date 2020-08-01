#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#

# @lc code=start
from bisect import insort_left
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]
        temp_items = []
        for x, y in enumerate(nums):
            num = y.pop(0)
            insort_left(temp_items, (num, x))
        left, right = temp_items[0][0], temp_items[-1][0]
        width = right - left

        while True:
            _, index = temp_items.pop(0)
            if nums[index]:
                num = nums[index].pop(0)
                insort_left(temp_items, (num, index))
                t_left, t_right = temp_items[0][0], temp_items[-1][0]
                t_width = t_right - t_left
                if width > t_width:
                    left, right, width = t_left, t_right, t_width
            else:
                return [left, right]
        
# @lc code=end


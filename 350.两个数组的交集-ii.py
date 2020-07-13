#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [*(Counter(nums1) & Counter(nums2)).elements()]
# @lc code=end


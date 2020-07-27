#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        
        def check_mid(mid):
            num = 1
            s = 0
            for i in nums: 
                if s + i > mid:
                    s = i
                    num += 1
                else:
                    s += i
            return num > m
        
        while left < right:
              mid = (left + right) // 2
              res = check_mid(mid)
              if res:
                  left = mid + 1
              else:
                  right = mid
        return left
# @lc code=end


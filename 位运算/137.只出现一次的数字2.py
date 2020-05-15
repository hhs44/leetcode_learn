from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for x, y in enumerate(nums):
            if y not in nums[:x] + nums[x+1:]:
                print(y)

if __name__ == '__main__':
    nums =[2,2,1]
    Solution().singleNumber(nums)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for x, y in enumerate(nums):
        #     if y not in nums[:x] + nums[x+1:]:
        #         return y
        i = 0
        for x in nums:
            i ^= x
        return i

if __name__ == '__main__':
    nums =[2,2,1]
    print(Solution().singleNumber(nums))
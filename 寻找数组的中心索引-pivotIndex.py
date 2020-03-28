from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = sum(nums)
        lsum = 0
        for i, j in enumerate(nums):
            if lsum * 2 + j == res:
                return i
            lsum += j
        return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    num2 = [-1,-1,-1,-1,-1,-1]
    S = Solution().pivotIndex(num2)
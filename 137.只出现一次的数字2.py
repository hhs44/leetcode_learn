from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        datas = Counter(nums)
        for each in datas:
            if datas[each] == 1: return each


if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    print(Solution().singleNumber(nums))

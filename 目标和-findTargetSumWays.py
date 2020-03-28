from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # #解法一  会超时
        # """
        # :type nums: List[int]
        # :type S: int
        # :rtype: int
        # """
        # def helper(index: int, acc: int) -> int:
        #    if index == len(nums):
        #        if acc == S:
        #            return 1
        #        else:
        #            return 0
        #    return helper(index + 1, acc + nums[index]) + helper(index + 1, acc - nums[index])
        # return helper(0,0)

        # 解法二
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d, 0)
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
            dic = tdic
        return dic.get(S, 0)





if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    s = 3
    a = Solution().findTargetSumWays(nums,s)
    print(a)
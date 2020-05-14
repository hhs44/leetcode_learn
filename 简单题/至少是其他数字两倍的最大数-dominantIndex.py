from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        #         #解法一
        #         max_num = nums[0]
        #         max_index = 0
        #         for i in range(len(nums)):
        #             if nums[i]>max_num:
        #                 max_num=nums[i]
        #                 max_index=i

        #         for i in range(len(nums)):
        #             if i!=max_index and nums[i]*2>max_num:
        #                 return -1
        #         return max_index
        # 解法二
        max_num = float('-inf')
        max_index = 0
        second_max_num = float('-inf')

        # 找出最大数和第二大数
        for i in range(len(nums)):
            n = nums[i]
            if n > max_num:
                second_max_num = max_num
                max_num = n
                max_index = i
            else:
                if n > second_max_num:
                    second_max_num = n

        if max_num >= second_max_num * 2:
            return max_index
        else:
            return -1
if __name__ == '__main__':
    nums=[0, 0, 2, 3]
    print(Solution().dominantIndex(nums))
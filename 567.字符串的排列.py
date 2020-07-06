#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # for x,y in enumerate(s2) :
        #     if y in s1:
        #         if x + len(s1) <= len(s2):
        #             t = s2[x:x+len(s1)]
        #             if Counter(t) == Counter(s1):
        #                 return True
        # return False
        # # 2222
        # r1 = Counter(s1)
        # r2 = Counter()
        # l1, l2 = len(s1), len(s2)
        # temp = 0
        # x = y = 0
        # while y < l2 :
        #     r2[s2[y]] += 1
        #     if r2[s2[y]] == r1[s2[y]]:
        #         temp += 1
        #     if temp == len(r1):
        #         return True
        #     y += 1
        #     if y - x + 1 > l1:
        #         if r1[s2[x]] == r2[s2[x]]:
        #             temp -= 1
        #         r2[s2[x]] -= 1
        #         if r2[s2[x]] == 0:
        #             del r2[s2[x]]
        #         x += 1
        # return False
        count_dict = Counter(s1)
        m = len(s1)
        i = 0
        j = m - 1
        while j < len(s2):
            if Counter(s2[i:j+1]) == count_dict:
                return True
            i += 1
            j += 1
        return False


                
# @lc code=end


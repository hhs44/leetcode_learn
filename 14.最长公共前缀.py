#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if strs==[]:
        #     return res
        # res = ''
        # for x, y in enumerate(strs[0]):
        #     for item in strs:
        #         try:
        #             if item[x] != y:
        #                 return res
        #         except:
        #             return res
        #     res += y
        # return res
        
        """
        横向扫描
        """
        
    #     if not strs: return ""
        
    #     prefix, n = strs[0], len(strs)
    #     for i in range(1, n):
    #         prefix = self.dfd(prefix, strs[i])
    #         if not prefix: break
    #     return prefix
    
    # def dfd(self,str1, str2):
    #     length, index = min(len(str1), len(str2)), 0
    #     while index < length and str1[index] == str2[index]:
    #         index += 1
    #     return str1[:index]
        """
        纵向扫描
        """
        # if not strs:
        #     return ""
        
        # length, count = len(strs[0]), len(strs)
        # for i in range(length):
        #     c = strs[0][i]
        #     if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
        #         return strs[0][:i]
        
        # return strs[0]
        """
        分治
        """
        # def lcp(start, end):
        #     if start == end:
        #         return strs[start]

        #     mid = (start + end) // 2
        #     lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
        #     minLength = min(len(lcpLeft), len(lcpRight))
        #     for i in range(minLength):
        #         if lcpLeft[i] != lcpRight[i]:
        #             return lcpLeft[:i]

        #     return lcpLeft[:minLength]

        # return "" if not strs else lcp(0, len(strs) - 1)
        """
        二分法（在最短数组中）
        """
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]


# @lc code=end


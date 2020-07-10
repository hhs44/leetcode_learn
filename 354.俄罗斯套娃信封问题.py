#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        if envelopes == None or len(envelopes)==0: return 0
        envelopes.sort(key = lambda x: [x[0], -x[1]])
        temp = [0 for _ in range(len(envelopes))]
        res = 0
        for env in envelopes:
            start, end = 0, res
            while start < end:
                mid = start + ((end - start) // 2)
                if temp[mid] < env[1]:
                    start = mid + 1
                else:
                    end = mid
            temp[start] = env[1]
            if end == res:
                temp[res] = env[1]
                res += 1
        return res
# @lc code=end


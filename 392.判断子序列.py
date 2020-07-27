#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = q = 0
        cnt = 0
        while p<len(s) and q<len(t):
            if s[p] == t[q]:
                cnt += 1
                p += 1
            q += 1
        return cnt == len(s)
# @lc code=end


#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def palindrome(s, l ,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r -= 1
            return s[l+1: r-l-1] 
        for i in range(len(s)):
            s1 = palindrome(s, i, i)
            s2 = palindrome(s, i, i+1)
            res = res if len(res) > len(s1) else s1
            res = res if len(res) > len(s2) else s2
        return res
# @lc code=end


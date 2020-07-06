#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [-1]
        for i, j  in enumerate(s):
            if j == "(":
                stack.append(i)
            elif len(stack) > 1:
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack[0] = i
        return ans
# @lc code=end


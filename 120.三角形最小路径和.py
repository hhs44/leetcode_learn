#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        rows = len(triangle)
        for i in range(rows-2, -1, -1):
            cols = len(triangle[i])
            for j in range(cols):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        return dp[0]

# @lc code=end


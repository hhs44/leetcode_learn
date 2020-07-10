#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        res = 0
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return pow(res, 2)
# @lc code=end


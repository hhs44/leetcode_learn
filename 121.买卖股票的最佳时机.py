#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices :return 0
        dp = [0]*(len(prices) + 1)
        for i in range(2, len(prices) + 1):
            dp[i] = max(dp[i-1], prices[i-1] - min(prices[:i-1]))
        return dp[-1]
# @lc code=end


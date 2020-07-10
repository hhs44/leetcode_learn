/*
 * @Author: WSGHuang 
 * @Date: 2020-07-10 11:59:00 
 * @Last Modified by:   WSGHuang 
 * @Last Modified time: 2020-07-10 11:59:00 
 */
#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, dp_i_0, dp_i_1, dp_pre_0 = len(prices), 0, float("-INF"), 0
        for i in range(0, n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = temp
        return dp_i_0 
# @lc code=end


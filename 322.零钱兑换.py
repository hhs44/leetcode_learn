#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 带备忘录
        memo = dict()
        # 获取金额n 需要的硬币数量
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')

            for coin in coins:
                subdp = dp(n - coin)
                # 若子问题无解
                if subdp == -1 :continue
                #  进行选择选择硬币最少的结果
                res = min(res, 1 + subdp)
            # 记录备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]     
        return dp(amount)

            
# @lc code=end


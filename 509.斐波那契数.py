
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        if N == 0 :return 0
        if N == 1 or N == 2: return 1
        pre, curr, res = 1, 1, 0
        for i in range(3,N+1):
            res = pre + curr
            pre = curr
            curr = res
        return res
            
# @lc code=end


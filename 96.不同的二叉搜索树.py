#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        d = [1] + [0] * n
        for i in range(1, n + 1):
            d[i] = sum(d[j] * d[i - 1 - j] for j in range(i))
        return d[n]
# @lc code=end


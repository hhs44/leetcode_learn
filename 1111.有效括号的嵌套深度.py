#
# @lc app=leetcode.cn id=1111 lang=python3
#
# [1111] 有效括号的嵌套深度
#

# @lc code=start
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        count = 0
        res = []
        for c in seq:
            if c == '(':
                count += 1
                res.append(count & 1)
            else:
                res.append(count & 1)
                count -= 1
        return res
# @lc code=end


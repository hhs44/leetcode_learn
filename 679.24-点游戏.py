#
# @lc app=leetcode.cn id=679 lang=python3
#
# [679] 24 点游戏
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        _zero = 1e-6
        def helper(ns):
            if not ns: return False
            if len(ns) == 1:return abs(24-ns[0]) <= _zero
            for i, n0 in enumerate(ns):
                for j, n1 in enumerate(ns):
                    if i == j:continue
                    new_1 = [tmp for idx, tmp in enumerate(ns) if idx not in [i, j]] if len(ns) > 2 else []
                    if i < j and helper(new_1 + [n0+n1,]):return True
                    if helper(new_1 + [n0-n1,]):return True
                    if i < j and helper(new_1+[n0*n1],):return True
                    if n1 > _zero and helper(new_1+[n0/n1],):return True
            return False
        return helper(nums)
# @lc code=end


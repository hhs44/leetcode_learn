#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = num1[::-1]
        b = num2[::-1]
        res = 0

        for i, x in enumerate(b):
            temp_res = 0
            for j, y in enumerate(a):
                temp_res += int(x) * int(y) * 10 ** j
            res += temp_res * 10 ** i

        return str(res)
# @lc code=end


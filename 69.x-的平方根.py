'''
@Author: your name
@Date: 2020-07-09 14:34:06
@LastEditTime: 2020-07-09 14:37:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode-learn\69.x-的平方根.py
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 :return 0
        z = x
        temp = 0
        while int(z) != temp:
            temp = int(z)
            z -= (z*z - x) / (2 * z)
        return int(z)
# @lc code=end


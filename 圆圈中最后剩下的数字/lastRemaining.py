"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
"""
#
# 问题1：当m>n时
# 问题2：时间
# 使用数组时

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # #失败方法，超时。
        # res = []
        # for x in range(0, n):
        #     res.append(x)
        # while len(res) > 2:
        #     if m % len(res) == 0:
        #         res = res[:m % len(res) - 1]
        #     else:
        #         res = res[m % len(res):] + res[:m % len(res) - 1]
        #
        # return res[m % 2]

        # 约瑟夫环？？？
        x = 0
        for i in range(2, n + 1):
            x = (m + x) % i
        return x

if __name__ == '__main__':
    Solution().lastRemaining(9,13)

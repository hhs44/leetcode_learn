# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#
#  
#
# 示例：
#
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
#
# 提示：
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # i = 0
        # start = 0
        # y = 1
        # while start < len(A):
        #     a = sum(A[start:y])
        #     if (a % K) == 0:
        #         print(A[start:y])
        #         i += 1
        #         y += 1
        #     else:
        #         y += 1
        #     if y > len(A):
        #         start += 1
        #         y = start + 1
        #         continue
        # return i
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 000)
            ans += same
            record[modulus] = same + 1
        return ans


if __name__ == '__main__':
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    print(Solution().subarraysDivByK(A, K))

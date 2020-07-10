#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not  matrix:
            return []
        res = []
        row ,clo = len(matrix),len(matrix[0])
        x1, y1, x2, y2 = 0, 0, clo - 1, row - 1
        while x1<=x2 and y1 <=y2:
            for i in range(x1,x2+1):
               res.append(matrix[y1][i])
            for j in range(y1+1, y2+1):
                res.append(matrix[j][x2])
            if x1 < x2 and y1 < y2:
                for i in range(x2-1, x1, -1):
                    res.append(matrix[y2][i])
                for j in range(y2, y1, -1):
                    res.append(matrix[j][x1])
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return res
# @lc code=end


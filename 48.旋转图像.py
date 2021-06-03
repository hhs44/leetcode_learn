#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i,row in enumerate(matrix):
            for j,col in enumerate(row):
                if i > j :
                    tmp = col
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
        for i,row in enumerate(matrix):
            row.reverse()
# @lc code=end


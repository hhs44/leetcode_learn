#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        temp = [0 for x in range(0, m)]
        temp[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(0,n):
            for j in range(0,m):
                if obstacleGrid[i][j] == 1:
                    temp[j] = 0
                    continue
                if (j - 1) >= 0 and obstacleGrid[i][j - 1] == 0:
                    temp[j] += temp[j - 1]
        return temp.pop()
# @lc code=end


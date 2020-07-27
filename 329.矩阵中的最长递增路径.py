#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        row, col = len(matrix), len(matrix[0])

        visited = [[None]*(col) for i in range(row)]

        m = 0 

        def search_nearby(i,j):
            nonlocal m

            temp = [] 

            if i != 0 and matrix[i-1][j] > matrix[i][j]: 
                temp.append(visited[i-1][j]) if visited[i-1][j] else temp.append(search_nearby(i-1,j))

            
            if j != 0 and matrix[i][j-1] > matrix[i][j]: 
                temp.append(visited[i][j-1]) if visited[i][j-1] else temp.append(search_nearby(i,j-1))

            
            if i != row-1 and matrix[i+1][j] > matrix[i][j]: 
                temp.append(visited[i+1][j]) if visited[i+1][j] else temp.append(search_nearby(i+1,j))

        
            if j != col-1 and matrix[i][j+1] > matrix[i][j]: 
                temp.append(visited[i][j+1]) if visited[i][j+1] else temp.append(search_nearby(i,j+1))
            
            visited[i][j] = max(temp)+1 if temp else 1

            m = max(m,visited[i][j])
            return (visited[i][j])
        
        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    search_nearby(i,j)
        
        return m


# @lc code=end


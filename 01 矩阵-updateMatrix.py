from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 解法dfs
        #         if matrix==[]:
        #             return []

        #         m, n = len(matrix), len(matrix[0])
        #         vistied = [[float('inf')]*n for _ in range(m)]
        #         for i in range(m):
        #             for j in range(n):
        #                 if matrix[i][j] == 0:
        #                     vistied[i][j] = 0
        #                 elif i>0:
        #                     vistied[i][j] = min(vistied[i][j],vistied[i-1][j]+1)
        #                 elif j>0:
        #                     vistied[i][j] = min(vistied[i][j],vistied[i][j-1]+1)
        #         for i in range(m-1,-1,-1):
        #             for j in range(n - 1, -1, -1):
        #                 if matrix[i][j] == 0:
        #                     vistied[i][j] = 0
        #                 elif i< m-1:
        #                     vistied[i][j] = min(vistied[i][j],vistied[i+1][j]+1)
        #                 elif j< n-1:
        #                     vistied[i][j] = min(vistied[i][j],vistied[i][j+1]+1)

        #         return vistied
        # bfs

        if matrix == []:
            return []
        ans = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        queue = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                    queue.append((i, j))
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            i, j = queue.pop(0)
            for i_delta, j_delta in direction:
                r = i + i_delta
                c = j + j_delta
                if r >= 0 and r <= len(matrix) - 1 and c >= 0 and c <= len(matrix[0]) - 1 and ans[r][c] > ans[i][j] + 1:
                    ans[r][c] = ans[i][j] + 1
                    queue.append((r, c))

        return ans
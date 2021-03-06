from queue import Queue
from typing import List




class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 解法一
        q = Queue()
        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        row= len(grid)
        clo = len(grid[0])
        vistied = [[False for a in range(0, clo)] for b in range(0,row)]
        for i in range(row):
            for j in range(clo):
                if grid[i][j] == "1" and vistied[i][j] == False:
                    q.put([i, j])
                    vistied[i][j] = True
                    t = 1
                    while q.empty() == False:
                        site = q.get()
                        x = site[0]
                        y = site[1]
                        for k in range(0, len(directions)):
                            new_x = x + directions[k][0]
                            new_y = y + directions[k][1]
                            if 0 <= new_x < row and 0 <= new_y < clo:
                                if grid[new_x][new_y] == "1" and vistied[new_x][new_y] == False:
                                    vistied[new_x][new_y] = True
                                    t += 1
                                    q.put([new_x, new_y])
                    count = t if t > count else count
        print(vistied)
        return count
    #     # 解法二
    #     d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #     count = 0
    #     vistied = [[False for a in range(0, len(grid[0]))] for b in range(0, len(grid))]
    #     for i in range(0, len(grid)):
    #         for j in range(0, len(grid[0])):
    #             if grid[i][j] == "1":
    #                 count += 1
    #                 self.find(grid, i, j)
    #     return count

    # def find(self, grid: List[List[str]], i, j):
    #     if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
    #         grid[i][j] = "0"
    #         self.find(grid, i + 1, j)
    #         self.find(grid, i - 1, j)
    #         self.find(grid, i, j + 1)
    #         self.find(grid, i, j - 1)





if __name__ == '__main__':
    # list =[[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
    list = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    list1 = [["0","1"]]
    list2 = [
        ["1","0","0","1","1","1","0","1","1","0","0","0","0","0","0","0","0","0","0","0"],
        ["1","0","0","1","1","0","0","1","0","0","0","1","0","1","0","1","0","0","1","0"],
        ["0","0","0","1","1","1","1","0","1","0","1","1","0","0","0","0","1","0","1","0"],
        ["0","0","0","1","1","0","0","1","0","0","0","1","1","1","0","0","1","0","0","1"],
        ["0","0","0","0","0","0","0","1","1","1","0","0","0","0","0","0","0","0","0","0"],
        ["1","0","0","0","0","1","0","1","0","1","1","0","0","0","0","0","0","1","0","1"],
        ["0","0","0","1","0","0","0","1","0","1","0","1","0","1","0","1","0","1","0","1"],
        ["0","0","0","1","0","1","0","0","1","1","0","1","0","1","1","0","1","1","1","0"],
        ["0","0","0","0","1","0","0","1","1","0","0","0","0","1","0","0","0","1","0","1"],
        ["0","0","1","0","0","1","0","0","0","0","0","1","0","0","1","0","0","0","1","0"],
        ["1","0","0","1","0","0","0","0","0","0","0","1","0","0","1","0","1","0","1","0"],
        ["0","1","0","0","0","1","0","1","0","1","1","0","1","1","1","0","1","1","0","0"],
        ["1","1","0","1","0","0","0","0","1","0","0","0","0","0","0","1","0","0","0","1"],
        ["0","1","0","0","1","1","1","0","0","0","1","1","1","1","1","0","1","0","0","0"],
        ["0","0","1","1","1","0","0","0","1","1","0","0","0","1","0","1","0","0","0","0"],
        ["1","0","0","1","0","1","0","0","0","0","1","0","0","0","1","0","1","0","1","1"],
        ["1","0","1","0","0","0","0","0","0","1","0","0","0","1","0","1","0","0","0","0"],
        ["0","1","1","0","0","0","1","1","1","0","1","0","1","0","1","1","1","1","0","0"],
        ["0","1","0","0","0","0","1","1","0","0","1","0","1","0","0","1","0","0","1","1"],
        ["0","0","0","0","0","0","1","1","1","1","0","1","0","0","0","1","1","0","0","0"]
    ]
    # Solution.data_write('./content/test.xlsx',list2)
    count = Solution().numIslands(list1)
    print(count)


from queue import Queue

from matplotlib.mathtext import List


class Solution:
    def wallsAndGates(rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        # ordin = [[0,1],[0,-1],[1,0],[-1,0]]
        # q =Queue()
        # for i in range(0,len(rooms)):
        #     for j in range(0,len(rooms[0])):
        #         if rooms[i][j]==0:
        #             q.put([i,j])
        # while q.empty()==False:
        #     site= q.get()
        #     i = site[0]
        #     j = site[1]
        #     for k in range(0,len(ordin)):
        #         x = i + ordin[k][0]
        #         y = j + ordin[k][1]
        #         if x >= 0 and x <len(rooms) and y>=0 and y<len(rooms[0]) and rooms[x][y]>rooms[i][j]+1:
        #             rooms[x][y]=rooms[i][j]+1
        #             q.put([x,y])
        #解法二
        row, col = len(rooms), len(rooms[0])
        # find the index of a gate
        q = [(i, j) for i in range(row) for j in range(col) if rooms[i][j] == 0]
        for x, y in q:
            # get the distance from a gate
            distance = rooms[x][y]+1
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for dx, dy in directions:
                # find the INF around the gate
                new_x, new_y = x+dx, y+dy
                if 0 <= new_x < row and 0 <= new_y < col and rooms[new_x][new_y] == 2147483647:
                    # update the value
                    rooms[new_x][new_y] = distance
                    q.append((new_x,  new_y))

if __name__ == '__main__':
    rooms = [[56565,-1,0,21321],[2123,123331,3233,12321,-1],[1232,-1,2312431,-1],[0,-1,23231,12432131]]
    print(rooms)
    newrooms = Solution.wallsAndGates(rooms)
    print(rooms)


from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        init = image[sr][sc]

        def find(sr,sc):
            if 0 <= sr< len(image) and 0 <= sc < len(image[0]) and image[sr][sc]==init:
                image[sr][sc]=newColor
                find(sr+1,sc,)
                find(sr-1,sc,)
                find(sr,sc+1,)
                find(sr,sc-1,)
        if init == newColor:
            return image
        find(sr,sc)

image = [[0,0,0],[0,1,1]]
if __name__ == '__main__':
    s = Solution()
    print(s.floodFill(image,1,1,1))
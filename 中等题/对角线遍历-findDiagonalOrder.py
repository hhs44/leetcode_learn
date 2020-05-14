from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        def revers(k,x):
            i = x
            j=k
            temp = []
            while 0 <= i < m and 0 <= j < n:
                temp.append(matrix[i][j])
                i += 1
                j -= 1
            if (x+k)%2==0:
                for k in range(len(temp)):
                    res.append(temp.pop(-1))
            else:
                for k in range(len(temp)):
                    res.append(temp.pop(0))

        res = []
        while len(res)<(m*n):
            if m==1 or n==1:
                for i in range(m):
                    for j in range(n):
                        res.append(matrix[i][j])
                return res
            for k in range(n):
                x = 0
                revers(k,x)
            for k  in range(1,m):
                if k>=m:
                    return res
                revers(n-1,k)
        return res
            # while k == m-1:
            #     b = k
            #     x+=1
            #     a=x
            #     if k == m-1 and x == n-1:
            #         res.append(matrix[k][x])
            #         return res
            #     while 0 <= a<m and 0 <= b <n:
            #         if (a+b)%2==0:
            #             res.append(matrix[b][a])
            #             a += 1
            #             b -= 1
            #         else:
            #             res.append(matrix[a][b])
            #             a += 1
        #             b -= 1

if __name__ == '__main__':

    nums = [[1,2,3],[4,5,6],[7,8,9]]
    nums1=[[2,3]]
    nums2=[[6,9,7]]
    nums3 = [[2, 5, 8], [4, 0, -1]]
    print(Solution().findDiagonalOrder(nums3))
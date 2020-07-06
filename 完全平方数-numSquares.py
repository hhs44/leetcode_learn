from queue import Queue


class Solution:
    def numSquares(n) :

        # q = Queue()
        # visited = [False for _ in range(n + 1)]
        # visited[0]=True
        # i=0
        # while i**2 <n:
        #     i=i+1
        #     return i
        #
        # q.put(i)
        # count = 1
        # if
        # while q:
        #     count+=1
        #     site =q.get()
        #     new_s = n - site
        #     if


        q = list()
        q.append([n, 0])
        visited = [False for _ in range(n + 1)]
        visited[n] = True

        while any(q):
            num, step = q.pop(0)

            i = 1
            tNum = num - i ** 2
            while tNum >= 0:
                if tNum == 0:
                    return step + 1

                if not visited[tNum]:
                    q.append((tNum, step + 1))
                    visited[tNum] = True

                i += 1
                tNum = num - i ** 2

if __name__ == '__main__':

   a= Solution.numSquares(12)
   print(a)
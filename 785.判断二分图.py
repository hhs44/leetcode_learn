#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == 0: 
                color[i] = 1
                queue = deque()
                queue.append(i)
                while queue:
                    cur = queue.popleft()
                    col = color[cur]
                    for j in graph[cur]:
                        if color[j] == col:
                            return False
                        elif color[j] == -col:
                            continue
                        else:
                            color[j] = -col
                            queue.append(j)
        return True
# @lc code=end


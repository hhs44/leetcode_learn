#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, visited, flags):
            if flags[i] == -1:return True
            if flags[i] == 1:return False
            flags[i] = 1
            for j in visited[i]:
                if not dfs(j, visited, flags): return False
            flags[i] = -1
            return True
        visited = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            visited[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, visited, flags):return False
        return True
# @lc code=end


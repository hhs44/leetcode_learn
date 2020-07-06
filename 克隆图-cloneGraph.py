


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node: 'Node') -> 'Node':
        #解法一
        lookup = {}

        def dfs(node):
            # print(node.val)
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)


# from collections import deque
#         lookup = {}
#
#         def bfs(node):
#             if not node: return
#             clone = Node(node.val, [])
#             lookup[node] = clone
#             queue = deque()
#             queue.appendleft(node)
#             while queue:
#                 tmp = queue.pop()
#                 for n in tmp.neighbors:
#                     if n not in lookup:
#                         lookup[n] = Node(n.val, [])
#                         queue.appendleft(n)
#                     lookup[tmp].neighbors.append(lookup[n])
#             return clone
#
#         return bfs(node)



if __name__ == '__main__':
    node = {"$id": "1",
            "neighbors": [
                {"$id": "2",
                 "neighbors": [
                     {"$ref": "1"},
                     {"$id": "3",
                      "neighbors": [
                          {"$ref": "2"},
                          {"$id": "4",
                           "neighbors": [
                               {"$ref": "3"},
                               {"$ref": "1"}],
                           "val": 4}],
                      "val": 3}],
                 "val": 2},
                {"$ref": "4"}],
            "val": 1}

    a = Solution().cloneGraph(Node)
    print(a)

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # bfs
        # 使用栈
        # visited,stack={0},[0]
        # while stack:
        #     room_index = stack.pop()
        #     for key in rooms[room_index]:
        #         if key not in visited:
        #             visited.add(key)
        #             stack.append(key)
        # return len(visited)==len(rooms)

        # 使用递归 dfs
        # ed={}
        # def dfs(room_index,ed):
        #     ed.add(room_index)
        #     for key in rooms[rooms_index]:
        #         if key not in ed :
        #             dfs(key,ed)
        # dfs(0,ed)
        # return len(ed)==len(rooms)
        room_map = {0}  # 所有能进去的房间,首先能进去0房间

        def enterroom(keys):
            for key in keys:
                if key not in room_map:
                    room_map.add(key)
                    enterroom(rooms[key])
                else:
                    pass
            return

        enterroom(rooms[0])
        return len(room_map) == len(rooms)
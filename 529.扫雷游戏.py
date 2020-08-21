#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def helper(l, c, f=False):
            if f and board[l][c] == "M": board[l][c] = "X"; return 
            elif board[l][c] != "E": return
            nlocal, count = [], 0
            for a, b in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nl, nc = a+l, c+b
                if nl >= 0 and nl < len(board) and nc >= 0 and nc < len(board[l]):
                    if board[nl][nc] == "M": count += 1
                    nlocal.append((nl, nc))
            if count: board[l][c] = str(count);return
            else: board[l][c] = "B"
            for nl, nc in nlocal: helper(nl, nc)
        helper(click[0],click[1], True)
        return board
# @lc code=end


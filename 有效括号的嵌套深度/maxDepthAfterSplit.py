"""
输入：seq = "(()())"
输出：[0,1,1,1,1,0]
"""
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        count = 0
        res = []
        for c in seq:
            if c == '(':
                count += 1
                res.append(count & 1)
            else:
                res.append(count & 1)
                count -= 1
        return res
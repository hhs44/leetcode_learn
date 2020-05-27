#
# 小时：8 4 2 1
# 分钟：32 16 8 4 2 1
#
# 输入亮灯数目，返回可以表示的时间
#
# 输入: n = 1
# 返回: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
#
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        if num < 0:
            return []

        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == num:
                    res.append(f'{h}:{m:0>2d}')
        return res

if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
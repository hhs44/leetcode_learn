# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
#
# 示例：
#
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 说明：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
#

# 方法一：滑动窗口
# 第一步：滑动窗口的意思就是使用两个指针，一个用于向外探索，一个用于从开始位置缩小窗口
# 第二步：先用一个哈希表表示t中所有字符以及他们的个数，再设置一个哈希表动态维护窗口中
# 所有字符和个数，如果该动态表中包含t哈希表中所有字符且字符的个数不小于t哈希表中的个字符
# 数目，那么这个窗口时可行的
from collections import Counter
from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = s + s
        n = len(s)
        target = Counter(t)
        counter = defaultdict(lambda: 0)

        def contains(counter, target):
            if len(counter) < len(target):
                return False
            for k in counter:
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for r in range(n):
            if s[r] in target:
                counter[s[r]] += 1
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans):
                    ans = s[l:r + 1]
                if s[l] in target:
                    counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans

#
# @lc app=leetcode.cn id=911 lang=python3
#
# [911] 在线选举
#

# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        l = len(times)
        self.time = times
        self.winner = []
        d = dict()
        winner_now = persons[0]
        max_ticket = 1
        d[persons[0]] = 1
        for i in range(len(persons)):
            if persons[i] in d:
                d[persons[i]] += 1
            else:
                d[persons[i]] = 1
            if d[persons[i]] >= max_ticket:
                winner_bynow = persons[i]
                max_ticket = d[persons[i]]
            self.winner[i] = winner_now


    def q(self, t: int) -> int:
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end


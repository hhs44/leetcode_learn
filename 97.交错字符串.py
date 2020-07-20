#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if "" in (s1, s2):return s3 in (s1, s2)
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):return False
        minJ=0
        maxJ = [c1==c2 for c1,c2 in zip(s2+'$',s3)].index(False)
        dp = [True]*(maxJ+1) + [False]*(l2-maxJ)  #首行
        #遍历完成后： dp[j] == isInterleave(s1,s2[:j],s3[len1+j:])
        for i in range(l1):
            while (minJ <= maxJ) and (not dp[minJ]):
                minJ += 1
            if minJ > maxJ:return False
            dp[minJ] = s1[i]==s3[i+minJ]
            for j in range(minJ,maxJ):
                dp[j+1] = (dp[j+1] and s1[i]==s3[i+j+1]) or (dp[j] and s2[j]==s3[i+j+1])
            while maxJ<l2 and dp[maxJ] and s2[maxJ]==s3[i+maxJ+1]:
                maxJ+=1
                dp[maxJ]=True
        return dp[-1]

# @lc code=end


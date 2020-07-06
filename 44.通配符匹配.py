#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:return not s
        #双指针
        i=j = i_shadow = 0
        #'s'匹配的位置
        start = -1  #*出现的位置
        while i <len(s):
            if j<len(p) and p[j] in {s[i],'?'}:
                i+=1
                j+=1
            #如果遇到’*‘ 先按匹配空字符处理，在不断向后扩展。
            elif j<len(p) and p[j]=='*':
                start = j
                i_shadow = i
                j += 1
            #不断扩展i,直到遇到一个s[i]==('*'号后面的字符)，然后再继续匹配
            elif start != -1:
                j = start+1
                i_shadow +=1
                i = i_shadow
            else:
                return False
        #s匹配完成，p可能还没有遍历完，进一步处理
        for x in p[j:]:
            if x !='*':
                return False
        return True
# @lc code=end


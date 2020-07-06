from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = ""
        if not start:
            return start
        i = 0
        j = 0
        while True:
            x=strs[i][j]
            while i<len(strs)-1:
                i+=1
                if x == strs[i][j]:
                    continue
                else:
                    return start
            if i==len(strs)-1:
                start+=x
                i=0
                j+=1

if __name__ == '__main__':
   a =  ["flower", "flow", "flight"]
   b=[]
   print(Solution().longestCommonPrefix(b))
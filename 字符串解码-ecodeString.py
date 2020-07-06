class Solution:
    def decodeString(self, s: str) -> str:
        rep = []
        num = 0
        st =''
        for i in s:
            if i.isdigit():
                num =num*10 +int(i)
            elif i == '[':
                rep.append(st)
                rep.append(num)
                st = ''
                num = 0
            elif i ==']':
                re_num = rep.pop()
                re_st = rep.pop()
                st =re_st +re_num*st
            else:
                st+=i
        return st
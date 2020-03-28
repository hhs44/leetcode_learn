class Solution:
    def addBinary(self, a: str, b: str) -> str:
        en =0
        sum=0
        i=len(a)-1
        j=len(b)-1
        res=""
        while j>=0 or i>=0 or en==1:
            if 0<=i and 0<=j :
                sum = en+int(b[j])+int(a[i])
                if sum > 1:
                    en = 1
                    res += str(sum % 2)
                else:
                    en = 0
                    res += str(sum % 2)
                i-=1
                j-=1
            elif i<0 and j>=0:
                sum= en+int(b[j])
                if sum > 1:
                    en = 1
                    res += str(sum % 2)
                else:
                    en = 0
                    res += str(sum % 2)
                j-=1
            elif j<0 and i>=0:
                sum= en+int(a[i])
                if sum > 1:
                    en = 1
                    res += str(sum % 2)
                else:
                    en = 0
                    res += str(sum % 2)
                i-=1
            else:
                en=0
                res+="1"

        return res[::-1]

if __name__ == '__main__':
    a="1010"
    b="1011"
    c="1111"
    d="1111"
    e="101111"
    f ="10"

    print(Solution().addBinary(e,f))
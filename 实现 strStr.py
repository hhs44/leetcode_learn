class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            i = 0
            for x in range(len(haystack)):
                j=x
                while i < len(needle) and x<len(haystack):
                    if haystack[x] == needle[i]:
                        i += 1
                        x += 1
                        if i == len(needle):
                            return j
                    else:
                        i=0
                        break
        else:
            return -1


if __name__ == '__main__':
    a = "mississippi"
    b = "issip"

    print(Solution().strStr(a, b))

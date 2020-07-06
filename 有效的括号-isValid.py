class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'{': '}', '[': ']', '(': ')'}
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif stack == []:
                return False
            elif d[stack[-1]] == i:
                stack.pop(-1)
        return stack == []


if __name__ == '__main__':
    s ="){"

    a = Solution.isValid(s)
    print(a)

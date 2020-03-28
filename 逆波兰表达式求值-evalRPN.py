from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        d = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        stack = []
        for i in tokens:
            if i in d:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(d[i](b, a)))
            else:
                stack.append(i)
        if len(stack) == 1:
            return stack.pop()
        else:
            return False


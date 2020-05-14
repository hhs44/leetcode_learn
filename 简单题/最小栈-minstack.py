class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if x is None:
            pass
        return self.stack.append(x)

    def pop(self) -> None:
        if (self.stack is None):
            return False
        self.stack.pop(-1)
        return True

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:

        return min(self.stack)

        return self.top()
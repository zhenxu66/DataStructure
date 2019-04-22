from collections import deque
# parallel stack remember and pop the smallest

class MinStack:
    # with deque
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = deque()     # python easy to use stack
        self.queue_min = deque()  # updated the top with compared smaller result

    def push(self, x: int) -> None:
        self.queue1.append(x)
        if not self.queue_min or self.queue_min[-1] > x:
            self.queue_min.append(x)
        else:
            self.queue_min.append(self.queue_min[-1])

    def pop(self) -> None:
        self.queue1.pop()
        self.queue_min.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def getMin(self) -> int:
        return self.queue_min[-1]


class MinStack2:

    # only with list
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []    # python easy to use stack
        self.queue_min = []  # updated the top with compared smaller result

    def push(self, x: int) -> None:
        self.queue1.append(x)
        if not self.queue_min or self.queue_min[-1] > x:
            self.queue_min.append(x)
        else:
            self.queue_min.append(self.queue_min[-1])

    def pop(self) -> None:
        self.queue1.pop()
        self.queue_min.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def getMin(self) -> int:
        return self.queue_min[-1]


class MinStack3:

    # only with list, not able to remember the previous min if the min index get pop()
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []  # python easy to use stack
        self.queue_min = None

    def push(self, x: int) -> None:
        self.queue1.append(x)
        if not self.queue_min or self.queue_min > x:
            self.queue_min = x

    def pop(self) -> None:
        self.queue1.pop()

    def top(self) -> int:
        return self.queue1[-1]

    def getMin(self) -> int:
        return self.queue_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':

    minStack = MinStack2();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();
    minStack.pop();
    minStack.top();
    minStack.getMin();


from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = deque()
        self.size = size
        self.count = 0
        self.res = 0.0 # average results

    def next(self, val: int) -> float:

        self.window.append(val)

        # initialize the first add with size
        if self.count < self.size:
            # must add count first to none zero
            self.count += 1
            self.res = (val + self.res * (self.count-1))/self.count
        else:
            # take the previous res with the left element pop removed and add the new one
            removeleft = self.window.popleft()
            self.res = (self.res * self.size - removeleft + val)/self.size

        return self.res



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':

    minStack = MovingAverage(2);
    minStack.next(-2);
    minStack.next(1);
    minStack.next(-3);
    minStack.next(3);
    minStack.next(4);

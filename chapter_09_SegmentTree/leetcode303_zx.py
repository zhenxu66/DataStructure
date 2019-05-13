class NumArray:

    def __init__(self, nums):
        self._data = nums[:]
        self._tree = [None] * 2 * len(nums)
        self._n = len(self._data)

        def _build_segment_tree(nums):
            # initialize all leaves
            self._tree[self._n:] = nums[:]
            # Reversed order node stored from child branch results
            for i in range(self._n - 1, 0, -1):
                self._tree[i] = self._tree[2 * i] + self._tree[2 * i + 1]

        _build_segment_tree(nums)

    def sumRange(self, i: int, j: int) -> int:
        i, j = i + self._n, j + self._n
        sums = 0
        while i <= j:
            if i % 2 == 1:  # 左边多出一个不能成对的
                sums += self._tree[i]
                i += 1
            if j % 2 == 0:  # 右边多出一个不能成对的
                sums += self._tree[j]
                j -= 1
            i //= 2
            j //= 2
        return sums

    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == '__main__':

    NumArray = NumArray([-2, 0, 3, -5, 2, -1]);
    print(NumArray.sumRange(0, 2));
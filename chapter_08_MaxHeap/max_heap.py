from chapter_02_Array.array import Array


class MaxHeap:
    def __init__(self, arr=None, capacity=None):

        # heapify Array to Heap and save into _data,
        if isinstance(arr, Array):
            self._data = arr
            # find the parent of last leaf index, till the end of index=0, but range need to have extra 开区间，所以要用-1
            # 逐个下沉
            for i in range(self._parent(arr.get_size() - 1), -1, -1):
                self._sift_down(i)
            return
        if not capacity:
            self._data = Array()
        else:
            self._data = Array(capacity=capacity)

    def size(self):
        return self._data.get_size()

    def is_empty(self):
        return self._data.is_empty()

# (1) return parent and left/right child

    # 返回完全二叉树数组表示中，一个索引所表示的元素的父亲节点的索引 i-1 // 2, index start from 0
    def _parent(self, index):
        if index == 0:
            raise ValueError('index-0 doesn\'t have parent.')
        return (index - 1) // 2

    # 返回完全二叉树数组表示中，一个索引所表示的元素的左孩子节点的索引 2 * i + 1
    def _left_child(self, index):
        return index * 2 + 1

    # 返回完全二叉树数组表示中，一个索引所表示的元素的右孩子节点的索引 2 * i + 2
    def _right_child(self, index):
        return index * 2 + 2

# (2) add and find/extract element

    # add (last) 和父亲节点对比逐层上浮, add the most recent index shift_up
    def add(self, e):
        self._data.add_last(e)
        self._sift_up(self._data.get_size() - 1)

    def _sift_up(self, k):
        while k > 0 and self._data.get(k) > self._data.get(self._parent(k)):
            self._data.swap(k, self._parent(k))
            k = self._parent(k)
            # k sift up to 0 stop compare

    # extract max[0]: sway the last one with 0 and remove, then sift down
    def find_max(self):
        if self._data.get_size() == 0:
            raise ValueError('Can not find_max when heap is empty.')
        return self._data.get(0)

    def extract_max(self):
        ret = self.find_max()
        self._data.swap(0, self._data.get_size() - 1)
        self._data.remove_last()
        self._sift_down(0)
        return ret

    # extra element, parent compare to child, swap the maximum child
    def _sift_down(self, k):
        # k End Condition:k not stay in last leaf layer, no left child
        while self._left_child(k) < self._data.get_size():
            j = self._left_child(k)

            # Compare right and left child to find the max one, k has right child, j+1<size
            if j + 1 < self._data.get_size() and self._data.get(j + 1) > self._data.get(j):
                # 说明右孩子的值比左孩子的值大 j+=1
                j = self._right_child(k)
            # k 没有右孩子或者右孩子还要小
            # do not have right child or right child<left child, j is larger index, otherwise, update with right index
            # 此时self._data.get(j)是左孩子和右孩子中的最大值

            # no need to sift down
            if self._data.get(k) > self._data.get(j):
                break

            # By default otherwise swap, then evaluate sift down updated with new k (max child in j)
            self._data.swap(k, j)
            k = j

    def replace(self, e):
        ret = self.find_max()
        # 这样可以一次logn完成
        self._data.set(0, e)
        self._sift_down(0)
        return ret





if __name__ == '__main__':
    n = 10000000
    # n = 1000
    from time import time

    start_time1 = time()
    max_heap = MaxHeap()
    from random import randint
    for i in range(n):
        max_heap.add(randint(0, 1000))
    print('heap add: ', time() - start_time1) # head add:  57.48132228851318

    # check results must in sequence bigger and smaller
    # arr_pop = []
    # for i in range(n):
    #     arr_pop.append(max_heap.extract_max())
    # for i in range(n-1):
    #     if arr_pop[i] < arr_pop[i+1]:
    #         raise ValueError('Error')
    #
    # print("Test MaxHeap completed.")

    start_time2 = time()
    arr = Array()
    from random import randint
    for i in range(n):
        arr.add_last(randint(0, 1000))
    max_heap = MaxHeap(arr)
    print('heapify: ', time() - start_time2) # heapify:  46.80660963058472

    def testHeap(arr, isheapify):
        start__time = time()

        if(isheapify):
            max__heap = MaxHeap(arr)
        else:
            max__heap = MaxHeap()
            for i in range(len(arr)):
                max__heap.add(i)

        arr_pop = []
        for i in range(n):
            arr_pop.append(max_heap.extract_max())
        for i in range(n-1):
        if arr_pop[i] < arr_pop[i+1]:
            raise ValueError('Error')
        print("Test MaxHeap completed.")

        return time() - start__time


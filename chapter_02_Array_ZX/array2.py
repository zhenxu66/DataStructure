class array:
    def __init__(self, arr= None, capacity =10):
        self._data = arr[:]
        self._size = len(arr)
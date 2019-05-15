from collections import defaultdict

_INIT_CAPACITY = 97

class HashTable:
    def __init__(self, M = _INIT_CAPACITY):
        self._M = M
        self._size = 0  # how many elements stored in HashTable
        self._hashtable = [defaultdict() for _ in range(M)]  # Good distribution M tree dict


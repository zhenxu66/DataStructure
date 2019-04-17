class Array:
    def __init__(self, arr=None, capacity=10): #like a construct function
        if isinstance(arr, list): #initilize with a list
            self._data = arr[:]   #_data is data/memory space inside the Array need to be fixed, len(_data) is the size
            self._size = len(arr)
            #_size number of data points, also is the pointer/index for next position
            return

        self._data = [None]*capacity #All with None type space
        self._size = 0
        # size = 0 point to first element, =1 point to second empty space but only one element inside

    def get_size(self):
        return self._size  #with real data inside


    def get_capacity(self):
        return len(self._data) #space opened

    def is_empty(self):
        # if self._size == 0:
        #     return True
        # else:
        #     return False

        return self._size == 0


    def add_last(self, e):
        # if(self._size == len(self._data)):
        #     raise ValueError('add failed. Array is full')
        # """从后往前遍历 往后挪一个位置"""
        # self._data[self._size] = e
        # self._size += 1


        self.add(self._size, e)


    def add_first(self, e):
        self.add(0, e)


    def add(self, index, e): #this index include 0, same as array index
        #python自动支持泛型,parameter canbe any type
        #length test, index range test, shift move, insert value, move size index to next one
        if(self._size == len(self._data)):
            raise ValueError('add failed. Array is full')
        if(index < 0 or index >self._size): # or not 0 <= index <= self._size
            raise ValueError('add failed. Require index >= 0 and index <= array sise.')
        #从后往前遍历 往后挪一个位置
        #add first element, no movement, skip this for loop
        for i in range(self._size-1, index-1, -1):
            # range like i=start_index, i=second value before it, loop by number2-number1-1 times
            self._data[i+1] = self._data[i]

        self._data[index] = e
        #insert the value of any type/object, JAVA need to have clear type class NAME<E>
        self._size += 1 # move the index



    def get(self, index): #index start from 0
        if(index < 0 or index >self._size):
            raise ValueError('add failed. Require index >= 0 and index <= array size.')
        return self._data[index]


    # def get_last(self):
    #
    #
    # def get_first(self):
    #
    #
    def set(self, index, e):
        if(index < 0 or index >self._size):
            raise ValueError('add failed. Require index >= 0 and index <= array size.')
        self._data[index] = e


    def contains(self, e):
        for i in range(0,self._size):
            if(self._data[i]==e):
                return True
        else:
            return False


    def find_index(self, e):
        for i in range(0,self._size):
            if(self._data[i]==e):
                return i
        else:
            return -1 #cannot find

    # def find_all_index(self, e):


    def remove(self, index):
        #index range test, shift move, insert value, move size index to next one
        if(index < 0 or index >self._size): # or not 0 <= index <= self._size
            raise ValueError('add failed. Require index >= 0 and index <= array sise.')
        #从后往前遍历 往后挪一个位置
        #add first element, no movement, skip this for loop
        res = self._data[index]
        for i in range(index, self._size-1, 1):
            # range like i=start_index, i=second value before it, loop by number2-number1-1 times
            self._data[i] = self._data[i+1]

        self._data[self._size]=None

        self._size -= 1 # move the index
        return res


    def remove_first(self):
        return self.remove(0)


    def remove_last(self):
        return self.remove(self._size-1)


    def remove_element(self, e):
        index = self.find_index(e)
        if(index !=-1):
            self.remove(index)
            return True
        else:
            False

    # def remove_all_element(self, e):



        # def _resize(self, new_capacity):
        #
        #
        # def swap(self, i, j):
        #
        #
    def __str__(self): #python toString in java like, print list directly (array in JAVA)
        return str('<chapter_02_Array.array.Array> : {}, capacity: {}'.format(self._data[:self._size], self.get_capacity()))

    def __repr__(self):
        return self.__str__()

if __name__ == '__main__':
    arr = Array()
    for i in range(0,5,1):
        arr.add_last(str(i))
    print(arr.get_capacity())
    print(arr.get_size())
    print(arr)
    # arr.add(5,100)
    arr.add_last('Cool')
    # print(arr.get(5))
    print(arr.get_capacity())
    print(arr.get_size())
    print(arr)
    # print(arr.contains(3))
    # print(arr.find_index(100))
    # print(arr.remove(5)) #same as remove_last() or arr.remove_element(100)
    # print(arr.remove_element(3))

    print(arr)
    print(arr.get_capacity())
    print(arr.get_size())

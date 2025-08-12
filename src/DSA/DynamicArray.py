class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self._size = 0
        self.arr = [None] * self.capacity

    def get(self, index):
        if index >= self._size or index < 0:
            return IndexError("Index out of bound")
        return self.arr[index]

    def set(self, index, value):
        if index >= self._size or index < 0:
            return IndexError("Index out of bound")
        self.arr[index] = value

    def size(self):
        return self._size

    def popback(self):
        if self._size > 0:
            self._size -= 1

    def resize(self, new_capacity):
        new_arr = [None] * self.capacity
        for i in range(self._size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def append(self, value):
        if self._size == len(self.arr):
            self.resize(self.capacity * 2)
        self.arr[self._size] = value
        self._size += 1


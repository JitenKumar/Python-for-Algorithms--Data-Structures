# Dynamic Array Implementation:
import ctypes


class DynamicArrays(object):

    def __init__(self):
        self.n = 0 # Count the elements in the arrays
        self.capacity = 2 # default capacity of the arrays
        self.Arr = self.make_array(self.capacity)

    # ge the len of the array
    def __len__(self):
        # It will return the no of elements in the array
        return self.n
    # get the item using the index

    def __getitem__(self,k):

        if not 0 <= k <= self.n:
            return IndexError
        # return the elements at index k
        return self.Arr[k]
    # append item at the end of the arrays

    def append(self,element):
        # if no of elements are equal to the full capacity
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.Arr[self.n] = element
        self.n += 1

    # if current arays is full then make new arrays
    def _resize(self,new_capacity):

        newarr = self.make_array(new_capacity)
        for k in range(self.n):
            newarr[k] = self.Arr[k]

        self.Arr = newarr
        self.capacity = new_capacity

    # this is used to make the arrays
    def make_array(self,new_capacity):
        return (new_capacity * ctypes.py_object)()


arr = DynamicArrays()
print(len(arr))
arr.append(1)
print(len(arr))
arr.append(3)
print(len(arr))
print(arr[1])
print(arr[1])
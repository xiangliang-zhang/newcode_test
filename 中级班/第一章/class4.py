class Heap:
    def __init__(self):
        self.value = []

    def get_parent_index(self, index):
        if index == 0 or index > len(self.value) - 1:
            return None
        else:
            return (index - 1) >> 1  # >> 二进制右移运算符,相当于除以2

    def swap(self, index1, index2):
        self.value[index1], self.value[index2] = self.value[index2], self.value[index1]

    def insert(self, data):
        self.value.append(data)
        index = len(self.value) - 1
        parent_index = self.get_parent_index(index)
        while parent_index is not None and self.value[parent_index] < data:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = self.get_parent_index()[parent_index]

    def removeMax(self):
        remove_data = self.value[0]
        self.value[0] = self.value[-1]
        del self.value[-1]

        self.heapify(0)
        return remove_data

    def heapify(self, index):
        total_index = len(self.value) - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and self.value[2 * index + 1] > self.value[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.value[2 * index + 2] > self.value[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


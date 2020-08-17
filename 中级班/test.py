# print(dict(enumerate([1, 2, 3, 4, 5])))
# print(4 >> 1)

# heap = [0 for i in range(4 + 1)]
# print(heap)

# test_list = [1, 2, 3, 4, 5]
# del test_list[0]
# print(test_list)
# print(sorted([1, 3, 2]))
# print(int(1.5))
import pandas as pd
import numpy as np

# tabel_test = pd.DataFrame(index=range(5), columns=range(5))

# dd = float("inf")
# print(dd)

# def cal(a, b):
#     i = min(a, b)
#     while i >= 2:
#         if a % i == 0 and b % i == 0:
#             a = a / i
#             b = b / i
#         i -= 1
#     return a, b
#
# print(cal(80, 90))

# print(4 % -2)
# tabel_test = pd.DataFrame(index=range(5), columns=range(5), data=np.nan)
# tabel_test.values[[np.arange(5)] * 2] = 0
# print(tabel_test)

# print(str(2.0))

# print(sorted([1, 3, 2]))
# list_TF = [[] for i in range(5)]
# print(list_TF)

# import numpy as np
#
# print(np.zeros((3)))

# arr = []
# print(not arr)

import math
import collections


class unionFindSet:
    def __init__(self, len):
        self.parents = []
        self.sizes = []
        for i in range(len):
            self.parents.append(i)
            self.sizes.append(1)

    def maxSize(self):
        ans = 0
        for size in self.sizes:
            ans = max(ans, size)

        return ans

    def findHead(self, element):
        stack = collections.deque()
        while element != self.parents[element]:
            stack.append(element)
            element = self.parents[element]

        while (self.parents is not None):
            self.parents[stack.popleft()] = element

        return element

    def union(self, a, b):
        aF = self.findHead(a)
        bF = self.findHead(b)
        if aF != bF:
            if self.sizes[aF] >= self.sizes[bF]:
                big = aF
            else:
                big = bF
            if big == aF:
                small = bF
            else:
                small = aF
            self.parents[small] = big
            self.sizes[big] = self.sizes[aF] + self.sizes[bF]


def largetsComponentSize(arr):
    unionFind = unionFindSet(len(arr))
    fatorsMap = collections.defaultdict(int)
    for i in range(len(arr)):
        num = arr[i]
        limit = int(math.sqrt(num))
        for j in range(1, limit + 1):
            if arr[i] % j == 0:
                if i != 1:
                    if j not in fatorsMap.keys():
                        fatorsMap[j] = i
                    else:
                        unionFind.union(i, j)

            other = arr[i] / j
            if other != 1:
                if other not in fatorsMap.keys():
                    fatorsMap[other] = i
                else:
                    unionFind.union(fatorsMap.get(other), i)


test = [2, 3, 6, 7, 4, 12, 21, 39]
print(largetsComponentSize(test))

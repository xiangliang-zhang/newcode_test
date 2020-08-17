# 并查集:两个集合,分别含有各自的数据.
# 操作1:查看两个元素是否在一个集合中.
# 操作2:合并两个元素. 将两个元素所在的集合中的所有元素放入一个集合当中.
# 操作3:找到根节点.

import math


class unionFindSet:
    def __init__(self, index):
        self.index = index
        self.parents = [0 for i in range(index)]
        self.sizes = [0 for i in range(index)]
        for i in range(index):
            self.parents[i] = i  # 初始化,每一个 元素下标 对应的父节点为 元素下标
            self.sizes[i] = 1  # 初始化,每一个父节点 对应元素个数 为 1

    def maxsize(self):
        print(self.sizes)
        return max(self.sizes)

    def find_parents(self, element):  # 传入的element 为index
        stack = []
        while element != self.parents[element]:  # 默认情况下,每个节点对应的父亲应该都是自己
            stack.append(element)  # 元素入栈,元素的父亲入栈,元素的爷爷入栈.
            element = self.parents[element]  # 获取这个元素的父亲
        while stack:
            self.parents[stack.pop(-1)] = element  # 不断出栈,统一修改父亲为上一个while循环中获取的element元素.
        return element

    def union(self, a, b):  # 这里传入的a,b参数也为index.
        aF = self.find_parents(a)
        bF = self.find_parents(b)
        if aF != bF:
            if self.sizes[aF] >= self.sizes[bF]:
                big = aF
                small = bF
            else:
                big = bF
                small = aF
            self.parents[small] = big
            self.sizes[big] = self.sizes[aF] + self.sizes[bF]


# a = [1, 2, 3, 4, 5]
# test = unionFindSet(a)
# test.union(1, 3)
# test.union(3, 5)
# test.union(3, 1)

# print(test.is_same_set(4, 5))


def answer(arr):
    if not arr:
        return
    length = len(arr)
    dict_test = {}
    union_test = unionFindSet(length)  # 实例化类
    for i in range(length):
        limit = int(math.sqrt(arr[i]))
        for j in range(1, limit + 1):
            if arr[i] % j == 0:
                if j != 1:
                    if j not in dict_test.keys():  # 如果当前值的因子不在列表中,就添加到里面
                        dict_test[j] = i
                    else:  # 如果当前值的因子在列表中,列表合并(使用的是index)
                        union_test.union(dict_test[j], i)

                other = arr[i] / j
                if other != 1:
                    if other not in dict_test.keys():
                        dict_test[int(other)] = i
                    else:
                        union_test.union(dict_test[other], i)

    return union_test.maxsize()


# b = [6, 2, 3, 102, 17]  # 5
c = [2, 3, 6, 7, 4, 12, 21, 39]  # 8
d = [100, 50, 17, 200]  # 3
e = [3, 2, 6, 9, 17, 13, 26]  # 6
# correct answer = 8
print(answer(c))

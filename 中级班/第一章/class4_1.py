class Heap:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


def getTopKSum(arr1, arr2, k):
    def heapInsert(heap, row, col, data, i):
        node = Heap(row, col, data)
        heap[i] = node
        parent = (i - 1) // 2
        while parent >= 0 and heap[parent].value < heap[i].value:  # 插入的值比父母节点大时
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent
            parent = (i - 1) // 2

    def popHead(heap, heapSize):
        res = heap[0]
        heap[0], heap[heapSize - 1] = heap[heapSize - 1], heap[0]
        heapify(heap, 0, heapSize - 1)
        return res

    def heapify(heap, i, heapSize):
        left = 2 * i + 1
        right = 2 * i + 2
        most = i
        while left < heapSize:
            if heap[left].value > heap[i].value:
                most = left
            if right < heapSize and heap[right].value > heap[most].value:
                most = right
            if most == i:
                break
            else:
                heap[most], heap[i] = heap[i], heap[most]
                i = most
                left = 2 * i + 1
                right = 2 * i + 2

    def isContains(row, col, posSet):
        return '_'.join([str(row), str(col)]) in posSet

    def addPosToSet(row, col, posSet):
        posSet.add('_'.join([str(row), str(col)]))

    if arr1 == None or arr2 == None or k < 1 or k > len(arr1) * len(arr2):
        return
    heap = [0 for i in range(k + 1)]  # 生成初始堆
    row = len(arr1) - 1  # 表格的行索引
    col = len(arr2) - 1  # 表格的列索引
    heapSize = 0
    heapInsert(heap, row, col, arr1[row] + arr2[col], heapSize)  # 将最大值加入堆
    heapSize += 1
    posSet = set()
    count = 0
    res = []  # 存放大根堆的根
    while count < k:
        cur = popHead(heap, heapSize)  # 出堆
        heapSize -= 1
        res.append(cur.value)
        r = cur.row  # 记录索引
        c = cur.col
        if not isContains(r - 1, c, posSet):  #加入最大值的左边
            heapInsert(heap, r - 1, c, arr1[r - 1] + arr2[c], heapSize)
            heapSize += 1
            addPosToSet(r - 1, c, posSet)
        if not isContains(r, c - 1, posSet):  # 加入最大值的上边
            heapInsert(heap, r, c - 1, arr1[r] + arr2[c - 1], heapSize)
            heapSize += 1
            addPosToSet(r, c - 1, posSet)
        count += 1
    return res


print(getTopKSum([3, 5, 7, 9, 11], [1, 2, 3, 4, 5], k=7))
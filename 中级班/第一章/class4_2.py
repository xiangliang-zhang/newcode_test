class Heap:
    def __init__(self, x=None, y=None, value=None):
        self.x = x
        self.y = y
        self.value = value


def insert(x, y, value, max_list):
    new_heap = Heap(x, y, value)
    max_list.append(new_heap)
    i = len(max_list) - 1
    parent = ((i - 1) >> 1)
    while new_heap.value > max_list[parent].value:
        max_list[i], max_list[int((i - 1) / 2)] = max_list[int((i - 1) / 2)], max_list[i]
        i = parent
        parent = ((i - 1) >> 1)


def record(index1, index2, record_list):
    record_list.append((index1, index2))


def sort_test(max_list, i, heapsize):
    left = 2 * i + 1
    right = 2 * i + 2
    most = 0
    while right < heapsize:
        if max_list[left].value > max_list[i].value:
            most = left
        if max_list[right].value > max_list[left].value:
            most = right
        if most == i:
            break
        max_list[most], max_list[i] = max_list[i], max_list[most]
        i = most
        left = 2 * i + 1
        right = 2 * i + 2


def popHead(max_list, res, heapsize):
    res.append(max_list[0])
    del max_list[0]
    # max_list[0], max_list[heapsize-1] = max_list[heapsize-1], max_list[0]
    sort_test(max_list, 0, heapsize-1)
    return res[-1]


def getTwoMax(arr1, arr2, k):
    if arr1 == None or arr2 == None or k < 1 or k > len(arr1) * len(arr2):
        return
    heapsize = 0
    a = len(arr1) - 1
    b = len(arr2) - 1
    max_list = []
    insert(a, b, arr1[a] + arr2[b], max_list)
    heapsize += 1
    record_list = []
    record(a, b, record_list)
    res = []
    while True:
        del_heap = popHead(max_list, res, heapsize)
        heapsize -= 1
        if (del_heap.x - 1, del_heap.y) not in record_list:
            insert(del_heap.x - 1, del_heap.y, arr1[del_heap.x - 1] + arr2[del_heap.y], max_list)
            heapsize += 1
            record(del_heap.x - 1, del_heap.y, record_list)
        if (del_heap.x, del_heap.y - 1) not in record_list:
            insert(del_heap.x, del_heap.y - 1, arr1[del_heap.x] + arr2[del_heap.y - 1], max_list)
            heapsize += 1
            record(del_heap.x, del_heap.y - 1, record_list)
        if len(res) == k:
            result = []
            for item in res:
                result.append(item.value)
            return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 5, 7, 9, 11]
k = 3
print(getTwoMax(arr1, arr2, 7))

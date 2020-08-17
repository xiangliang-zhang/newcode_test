arr = [1, 5, 3, 4, 2, 6, 7]
arr2 = []


def sort_length(arr):
    if not arr:
        return
    cur_max = float('-inf')
    list1 = []
    for i in range(len(arr)):
        cur = arr[i]
        if cur > cur_max:
            cur_max = cur
            continue
        else:
            list1.append(i)
    cur_min = float('inf')
    list2 = []
    for i in range(len(arr) - 1, -1, -1):
        cur = arr[i]
        if cur < cur_min:
            cur_min = cur
            continue
        else:
            list2.append(i)
    return max(list1) - min(list2) + 1


print(sort_length(arr2))

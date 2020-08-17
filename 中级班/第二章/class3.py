arr1 = [1, 1, 1, 1, 1, 1, 4]
arr3 = [1, 3, 2, 5]
arr2 = [3, 2, 5]


def func1(arr):
    if not arr:
        return
    else:
        arr.sort()
        result = 1
        for i in range(1, len(arr)):
            if arr[i] > result + 1:
                return result + 1
            else:
                result += arr[i]
        return result + 1


# print(func1(arr3))

def func2(arr):
    if not arr:
        return
    min_num = min(arr)
    sum_num = sum(arr)
    table_result = [[False for j in range(sum_num + 1)] for i in range(len(arr))]
    table_result[0][arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(1, sum_num + 1):
            if arr[i] == j:
                table_result[i][j] = True
            elif table_result[i - 1][j] and (i - 1 >= 0):
                table_result[i][j] = True
            elif table_result[i - 1][j - arr[i]] and (j - arr[i] > 0):
                table_result[i][j] = True

    ans = min_num
    for i in range(ans, sum_num+1):
        if not table_result[len(arr) - 1][i]:
            return i
    return sum_num + 1


print(func2([]))

arr = [3, 2, 4, 1, 4, 9, 5, 10, 1, 2, 2]
index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = 11
arr2 = [3, 3, 9, 2, 4, 7, 6, 8, 1, 5]

def operate(arr):
    if arr == None or len(arr) < 7:
        return False
    all = sum(arr)
    result_map = {}
    for i in range(1, len(arr) - 1):
        result_map[sum(arr[:i + 1])] = i
    lsum = arr[0]
    for a in range(1, len(arr) - 5):
        first = arr[a]
        if lsum + first + lsum in result_map.keys():
            value1 = result_map[lsum + first + lsum]
            second = arr[value1+1]
            if lsum + first + lsum + second +lsum in result_map.keys():
                value2 = result_map[lsum + first + lsum + second +lsum]
                third = arr[value2 + 1]
                if all - lsum - first - lsum - second - lsum - third == lsum:
                    return True
        else:
            lsum += arr[a]
    return False


print(operate(arr2))

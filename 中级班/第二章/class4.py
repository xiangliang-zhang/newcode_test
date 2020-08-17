def answer(arr, range_get):
    patches = []
    touch = 0
    if not arr:
        while range_get > touch:
            patches.append(touch + 1)
            touch += touch + 1
        return patches
    else:
        for i in range(len(arr)):
            while arr[i] > touch + 1:
                patches.append(touch + 1)
                touch += touch + 1
                if range_get < touch:
                    return patches
            touch = touch + arr[i]
            if range_get < touch:
                return patches
        while range_get > touch + 1:
            touch += touch + 1
            patches.append(touch + 1)

        return patches


args = [], 100
args2 = [3, 17, 21, 78], 67
print(answer(*args2))

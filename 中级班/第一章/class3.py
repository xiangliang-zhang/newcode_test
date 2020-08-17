def jump(list_test):
    step = 0
    curmaxright = 0
    nextmaxright = 0
    for item in range(len(list_test)):
        if curmaxright < item:
            step += 1
            curmaxright = nextmaxright
        else:
            nextmaxright = max(nextmaxright, item + list_test[item])

    return step

print(jump([2, 3, 2, 1, 2, 1, 5]))

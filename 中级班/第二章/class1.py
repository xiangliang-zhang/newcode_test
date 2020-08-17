# 递推思维
def get_answer(n):
    result_list = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    index = 1
    while index < n:
        result_list.append(min(2*result_list[i2], 3 * result_list[i3], 5 * result_list[i5]))
        if result_list[index] == 2 * result_list[i2]:
            i2 += 1
        if result_list[index] == 3 * result_list[i3]:
            i3 += 1
        if result_list[index] == 5 * result_list[i5]:
            i5 += 1
        index += 1
    return result_list[-1]

print(get_answer(10))
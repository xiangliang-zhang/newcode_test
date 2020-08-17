# 重点: 建二维表

def zhanzhuanxiangchu(a, b):
    min_num = min(a, b)
    max_num = max(a, b)
    r = max_num % min_num
    while r != 0:
        max_num = min_num
        min_num = r
        r = max_num % min_num
    return min_num


# def answer2(arrx, arry):
#     if len(arrx) != len(arry):
#         return
#     point_list = []
#     length = len(arrx)
#     for i in range(length):
#         point_list.append((arrx[i], arry[i]))
#     point_table = [[0 for i in range(length)] for i in range(length)]
#     for i in range(length):
#         for j in range(length):
#             # a, b, c = zhanzhuanxiangchu(point_list[j][1] - point_list[i][1], point_list[j][0] - point_list[i][0])
#             # point_table[i][j] = c + str(a) + '/' + str(b)
#
#     print(point_table)


# answer2([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])

print(zhanzhuanxiangchu(-3, 3))

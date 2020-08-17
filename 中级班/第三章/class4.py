#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/7 23:36
# @Author  : 一条很咸很咸的咸鱼

def isPerfectRectangle(rectangle):
    if not rectangle:
        return False
    area = 0
    x1 = float('inf')  # x1是最左边的x,要最小的
    x2 = float('-inf')  # x2是最右边的x,要最大的
    y1 = float('inf')  # y1是最下边的y,要最小的
    y2 = float('-inf')  # y2是最上面的y,要最大的
    hash_dict = {}
    for item in rectangle:
        x1 = min(x1, item[0])
        y1 = min(y1, item[1])
        x2 = max(x2, item[2])
        y2 = max(y2, item[3])
        area += (item[3] - item[1]) * (item[2] - item[0])
        str1 = str(item[0]) + '_' + str(item[1])
        str2 = str(item[0]) + '_' + str(item[3])
        str3 = str(item[2]) + '_' + str(item[1])
        str4 = str(item[2]) + '_' + str(item[3])
        hash_dict[str1] = 1 if str1 not in hash_dict else hash_dict[str1] + 1
        hash_dict[str2] = 1 if str2 not in hash_dict else hash_dict[str2] + 1
        hash_dict[str3] = 1 if str3 not in hash_dict else hash_dict[str3] + 1
        hash_dict[str4] = 1 if str4 not in hash_dict else hash_dict[str4] + 1

    hash_dict2 = {}
    for item in hash_dict.keys():
        if hash_dict[item] == 1:
            hash_dict2[item] = 1
    if (len(hash_dict2) != 4) or (str(x1) + '_' + str(y1) not in hash_dict2) or (
            str(x1) + '_' + str(y2) not in hash_dict2) or (str(x2) + '_' + str(y1) not in hash_dict2) or (
            str(x2) + '_' + str(y2) not in hash_dict2):
        return False
    return area == (x2 - x1) * (y2 - y1)


test1 = [[1, 1, 2, 2], [2, 1, 3, 2], [1, 2, 2, 3], [2, 2, 3, 3]]
print(isPerfectRectangle(test1))

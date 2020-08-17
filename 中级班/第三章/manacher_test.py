#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/3 17:57
# @Author  : 一条很咸很咸的咸鱼

# 时间复杂度O(N)
def manacher_test(str_test):
    if not str_test:
        return 0
    str_list = []
    for item in str_test:
        str_list.append('#')
        str_list.append(item)
    str_list.append('#')
    # print(str_list)
    radius = [0 for i in str_list]
    r = -1  # 初始化右边界的位置
    c = -1  # 初始化当前边界内的中心
    for p in range(len(radius)):
        if r > p:  # 如果右边界在当前位置的右边.
            radius[p] = min(radius[2*c-p], r-p+1)
        else:  # 右边界在当前位置的左边.
            radius[p] = 1
        while p + radius[p] < len(str_list) and p - radius[p] > -1:
            if str_list[p - radius[p]] == str_list[p + radius[p]]:
                radius[p] += 1
            else:
                break
        if p + radius[p] > r:
            r = p + radius[p] - 1
            c = p
    return max(radius) - 1



str_test = "abcba"
print(manacher_test(str_test))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/3 15:41
# @Author  : 一条很咸很咸的咸鱼

def answer(str_test):
    if not str_test:
        return 0
    str_list = []
    for item in str_test:
        str_list.append('#')
        str_list.append(item)
    str_list.append('#')
    r = -1
    c = -1
    radius = [0 for i in str_list]
    maxEnd = -1
    for i in range(len(str_list)):
        if i >= r:
            radius[i] = 1
        else:
            radius[i] = min(radius[2 * c - i], r - i + 1)
        while i + radius[i] < len(str_list) and i - radius[i] > -1:
            if str_list[i + radius[i]] == str_list[i - radius[i]]:
                radius[i] += 1
            else:
                break
        if i + radius[i] > r:
            r = i + radius[i] - 1
            c = i

        if r == len(str_list) - 1:  # 右边界等于生成列表的长度, 此时以c为中心的字符串的右边界已经到达最后一个字符.
            maxEnd = radius[i]
            break
    str_length = len(str_test) - maxEnd + 1  # 需要添加的字符串的长度
    res = []
    for i in range(str_length):
        res.append(str_list[2 * i + 1])
    return "".join(res)[::-1]


# str1 = 'A1BC22DE1F'
# print(answer(str1))
str2 = 'abccba'
print(answer(str2))

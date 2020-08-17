#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/9 16:04
# @Author  : 一条很咸很咸的咸鱼

def binaryFind(list_test, aim):
    l, r = 0, len(list_test) - 1
    result = []
    while l < r:
        if list_test[l] + list_test[r] > aim:
            r -= 1
        elif list_test[l] + list_test[r] < aim:
            l += 1
        elif list_test[l] + list_test[r] == aim:
            if (l == 0) or (list_test[l] != list_test[l - 1]):
                result.append((list_test[l], list_test[r]))
                l += 1
            else:
                l += 1
    return result


def thirdFind(list_test, aim):
    res = []
    for i in range(len(list_test) - 2):
        if i != 0 and list_test[i] == list_test[i - 1]:
            continue
        l, m, r = i, i + 1, len(list_test) - 1
        while m < r:
            if list_test[l] + list_test[m] + list_test[r] < aim:
                m += 1
            elif list_test[l] + list_test[m] + list_test[r] > aim:
                r -= 1
            elif list_test[l] + list_test[m] + list_test[r] == aim:
                if list_test[m] != list_test[m - 1] or m - 1 == l:
                    res.append((list_test[l], list_test[m], list_test[r]))
                    m += 1
                else:
                    m += 1
    return res


# print(binaryFind([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], 7))
# print(thirdFind([0, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6], 9))
print(binaryFind([-8, -4, -3, 0, 1, 2, 4, 5, 8, 9], 10))
print(thirdFind([-8, -4, -3, 0, 1, 2, 4, 5, 8, 9], 10))

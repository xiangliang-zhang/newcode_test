#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/23 17:22
# @Author  : 一条很咸很咸的咸鱼

def maxLength(arr):
    if not arr:
        return
    length = len(arr)
    max_length = 0
    for i in range(length):
        set = []
        for j in range(i, length):
            if arr[j] in set:
                break
            else:
                set.append(arr[j])
            if max(set) - min(set) == len(set) - 1:
                max_length = max(max_length, len(set))
    return max_length


arr = [5, 5, 3, 2, 6, 4, 3]
arr2 = [6, 8, 7, 7, 0, 1, 2, 3, 4, 5, 6]
arr3 = [3, 0, 1, 2, 4, 5]
arr4 = [7, 6, 8, 0, 7, 0, 5, 2, 3, 4, 1, 6]
print(maxLength(arr4))

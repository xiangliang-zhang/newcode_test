#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/23 23:38
# @Author  : 一条很咸很咸的咸鱼

# def prefix_table(pattern):
#     length_str = len(pattern)
#     prefix = [0 for i in range(length_str)]  # p[0]对应的prefix[0] = 0 默认
#     length = 0
#     i = 1
#     while i < length_str:
#         if pattern[i] == pattern[length]:
#             length += 1
#             prefix[i] = length
#             i += 1
#         else:
#             if length > 0:
#                 length = prefix[length - 1]
#             else:
#                 prefix[i] = length
#                 i += 1
#     if prefix:
#         prefix.pop(-1)
#     prefix.insert(0, -1)
#     return prefix
#
#
#
# def kmp_test(str1, str2):
#     if str1 == str2 or not str2:
#         return 0
#     next = prefix_table(str2)
#     i = 0
#     j = 0
#     while i < len(str1) and j < len(str2):
#         if (j == len(str2) - 1) and str1[i] == str2[j]:
#             return i - len(str2) + 1
#         if str1[i] == str2[j]:
#             i += 1
#             j += 1
#         else:
#             value = next[j]
#             if value == -1:
#                 i += 1
#                 j += 0
#             else:
#                 j = value
#     return -1
#
# print(kmp_test('a', ''))

def prefix_table(pattern):
    length_str = len(pattern)
    prefix = [0 for i in range(length_str)]  # p[0]对应的prefix[0] = 0 默认
    length = 0
    i = 1
    while i < length_str:
        if pattern[i] == pattern[length]:
            length += 1
            prefix[i] = length
            i += 1
        else:
            if length > 0:
                length = prefix[length - 1]
            else:
                prefix[i] = length
                i += 1
    if prefix:
        prefix.pop(-1)
    prefix.insert(0, -1)
    return prefix


# print(prefix_table('ababc'))

def kmp_test(str1, str2):
    next = prefix_table(str2)
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if (j == len(str2) - 1) and str1[i] == str2[j]:
            return i - len(str2) + 1
        if str1[i] == str2[j]:
            i += 1
            j += 1
        else:
            j = next[j]
            if j == -1:
                i += 1
                j += 1
    return -1


print(kmp_test('aaa', 'b'))

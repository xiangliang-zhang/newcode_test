#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/6/24 16:56
# @Author  : 一条很咸很咸的咸鱼

# KMP算法产生next数组:双指针 + 三种情况.
def gen_next(s):
    length = 0
    i = 1
    prefix_table = [0 for i in range(len(s))]
    while i < len(s):
        if s[i] == s[length]:
            length += 1
            prefix_table[i] = length
            i += 1
        else:
            if length > 0:
                length = prefix_table[length - 1]
            else:
                prefix_table[i] = length
                i += 1
    return prefix_table


# print(gen_next('aabaaac'))


def endNextLength(str_list):
    next = [0 for i in range(len(str_list) + 1)]
    next[0] = -1
    next[1] = 0
    pos = 2
    cn = 0
    while pos < len(str_list) + 1:
        if str_list[pos - 1] == str_list[cn]:
            cn += 1
            next[pos] = cn
            pos += 1
        elif cn > 0:
            cn = next[cn]
        else:
            next[pos] = 0
            pos += 1
    return next[-1]

# print(endNextLength('aabaaac'))

def answer(strtest):
    if not strtest:
        return ''
    strtest_list = list(strtest)
    if len(strtest_list) == 0:
        return strtest + strtest
    if len(strtest_list) == 2:
        if strtest_list[0] == strtest_list[1]:
            return strtest + strtest_list[0]
        else:
            return strtest + strtest
    endNext = endNextLength(strtest_list)
    return strtest + strtest[endNext:]


str_test1 = 'aaaa'
# str_test2 = 'aa'
# str_test3 = 'ab'
# str_test4 = 'abcdabcd'
# str_test5 = '123123'
print(answer(str_test1))
# print(answer(str_test2))
# print(answer(str_test3))
# print(answer(str_test4))
# print(answer(str_test5))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/6 22:24
# @Author  : 一条很咸很咸的咸鱼




def answer(str_input):
    return recursion_test(str_input, 0)[0]


def recursion_test(str_input, num):
    res = ''  # 存储每次递归{}内的内容
    times = 0  # 存储{}之前的数字
    while num < len(str_input) and str_input[num] != '}':
        if str_input[num] == '{':
            temp_res, num = recursion_test(str_input, num + 1)
            res += times * temp_res
            times = 0
            num += 1
        else:
            if '0' <= str_input[num] <= '9':
                times = 10 * times + int(str_input[num])  # 如果出现25{b}情况时就会用到
            if 'a' <= str_input[num] <= 'z':
                res += str_input[num]
            num += 1
    return res, num


test1 = '3{a}2{bc}'
test2 = "3{a2{c}}"
test3 = "2{abc}3{cd}ef"
test = '3{a}'
test4 = '0{a}'
print(answer(test4))

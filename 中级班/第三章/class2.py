#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/2 15:40
# @Author  : 一条很咸很咸的咸鱼

class Node:
    def __init__(self, val):
        self.val = val
        self.left = '#'
        self.right = '#'

def gen_next(str_test):
    if not str_test:
        return
    next_list = [0 for i in range(len(str_test))]
    pos = 1
    cur = 0
    while pos < len(str_test):
        if str_test[pos] == str_test[cur]:
            cur += 1
            next_list[pos] = cur
            pos += 1
        elif cur > 0:
            cur = next_list[cur - 1]
        else:
            next_list[pos] = 0
            pos += 1
    if next_list:
        next_list.insert(0, -1)
        return next_list
    else:
        return


def kmp_test(t1, t2):
    if not t2 or not t1:
        return
    next_list = gen_next(t2)
    i = 0
    j = 0
    while i < len(t1) and j < len(t2):
        if t1[i] == t2[j] or j == -1:
            i += 1
            j += 1
        else:
            j = next_list[j]
    if j == len(t2):
        return True
    else:
        return False

def isSubtree(t1, t2):  # 利用序列化的两个列表去KMP算法测试
    res1 = []
    res2 = []
    serialByPre(t1, res1)
    serialByPre(t2, res2)
    return kmp_test(res1, res2)

def serialByPre(head, res):  # 递归先序序列化树
    if head == None:
        res.append('#')
    else:
        if head == '#':
            res.append(head)
        else:
            res.append(head.val)
            serialByPre(head.left, res)
            serialByPre(head.right, res)

if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)
    t1.left.left.right = Node(8)
    t1.left.right.left = Node(9)

    t2 = Node(2)
    t2.left = Node(4)
    t2.left.right = Node(8)
    t2.right = Node(5)
    t2.right.left = Node(9)

    t3 = Node(1)
    t4 = Node(1)
    print(isSubtree(t3, t4))


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/8 23:28
# @Author  : 一条很咸很咸的咸鱼

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq

'''
heaqp模块提供了堆队列算法的实现，也称为优先级队列算法。
要创建堆，请使用初始化为[]的列表，或者可以通过函数heapify（）将填充列表转换为堆。
提供以下功能：
heapq.heappush（堆，项目）
将值项推入堆中，保持堆不变。
heapq.heapify（x）
在线性时间内将列表x转换为堆。
heapq.heappop（堆）
弹出并返回堆中的最小项，保持堆不变。如果堆是空的，则引发IndexError。
'''


def answer(lists):
    dummy = ListNode(0)
    p = dummy
    head = []

    # 依次把各个链表的头节点入小根堆
    for i in range(len(lists)):
        if lists[i]:
            # 入小根堆的结构为(val, i)
            heapq.heappush(head, (lists[i].val, i))
            lists[i] = lists[i].next  # 把下一个结点赋值给当前节点(用下一个节点覆盖当前节点?)  不存在越界情况,如果不存在 next=None.

    while head:
        val, idx = heapq.heappop(head)  # heappop默认弹出最小值
        p.next = ListNode(val)
        p = p.next  # p指针为结果链表中移动的指针
        if lists[idx]:
            heapq.heappush(head, (lists[idx].val, idx))
            lists[idx] = lists[idx].next  # 不断移动头指针往下一个指针移动
    return dummy.next

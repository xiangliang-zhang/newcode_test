#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/10 16:55
# @Author  : 一条很咸很咸的咸鱼

import sys

sys.setrecursionlimit(100000)  # 例如这里设置为十万


# 冒泡排序
# 时间复杂度O(N²)
# 空间复杂度O(1)
def bubbleSort(list_input):
    if not list_input or len(list_input) < 2:
        return list_input
    for i in range(len(list_input) - 1, -1, -1):
        for j in range(0, i):
            if list_input[j] > list_input[j + 1]:
                list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]
    return list_input


# 选择排序
def selectionSort(arr):
    if not arr or len(arr) < 2:
        return arr
    for i in range(len(arr) - 1):
        min_index = i
        # 每轮选择出最小的
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = i
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# 插入排序
def insertSort(arr):
    if not arr or len(arr) < 2:
        return arr
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            while arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


# 递归求一个数组的最大值问题
def getMax(arr, l, r):
    # 递归跳出的条件
    if l == r:
        return arr[l]
    mid = int((l + r) / 2)
    maxLeft = getMax(arr, l, mid)
    maxRight = getMax(arr, mid + 1, r)
    return max(maxLeft, maxRight)


# 归并排序
# 时间复杂度O(NlogN)
# 空间复杂度O(N)
def mergeSort(arr, l, r):
    if l == r:
        return
    mid = int((l + r) / 2)
    mergeSort(arr, l, mid)  # T(N/2)
    mergeSort(arr, mid + 1, r)  # T(N/2)
    merge(arr, l, mid, r)  # O(N)


def merge(arr, l, mid, r):
    help = []
    p1 = l
    p2 = mid + 1
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            help.append(arr[p1])
            p1 += 1
        else:
            help.append(arr[p2])
            p2 += 1

    while p1 <= mid:
        help.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help.append(arr[p2])
        p2 += 1
    for i in range(len(help)):
        arr[l + i] = help[i]


# 小和问题
def minSum(arr, l, r):
    if l == r:
        return 0
    mid = int((l + r) / 2)
    return minSum(arr, l, mid) + minSum(arr, mid + 1, r) + mergeSum(arr, l, mid, r)


def mergeSum(arr, l, mid, r):
    p1 = l
    p2 = mid + 1
    help_list = []
    res = 0
    while p1 <= mid and p2 <= r:
        if arr[p1] < arr[p2]:
            res += (r - p2 + 1) * arr[p1]
        if arr[p1] < arr[p2]:
            help_list.append(arr[p1])
            p1 += 1
        else:
            help_list.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help_list.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help_list.append(arr[p2])
        p2 += 1
    for i in range(len(help_list)):
        arr[l + i] = help_list[i]
    return res


# 逆序对问题
def merger_reverse_bin(arr, l, mid, r):
    p1 = l
    p2 = mid + 1
    help_list = []
    res = []
    while p1 <= mid and p2 <= r:
        if arr[p2] < arr[p1]:
            for i in range(mid - p1 + 1):
                res.append((arr[p1 + i], arr[p2]))
        if arr[p1] <= arr[p2]:
            help_list.append(arr[p1])
            p1 += 1
        else:
            help_list.append(arr[p2])
            p2 += 1
    while p1 <= mid:
        help_list.append(arr[p1])
        p1 += 1
    while p2 <= r:
        help_list.append(arr[p2])
        p2 += 1
    for i in range(len(help_list)):
        arr[l + i] = help_list[i]
    return res


def reverse_bin(arr, l, r):
    if l == r:
        return []
    mid = int((l + r) / 2)
    return reverse_bin(arr, l, mid) + reverse_bin(arr, mid + 1, r) + merger_reverse_bin(arr, l, mid, r)


if __name__ == '__main__':
    list1 = [2, 3, 4, 0, 7]
    list3 = [3, 7, 4, 8, 2]
    # list2 = [0]
    # print(bubbleSort(list3))
    # print(selectionSort(list3))
    # print(insertSort(list3))
    # list1 = [1, 2, 3, 4]
    # mergeSort(list1, 0, len(list1) - 1)
    # print(minSum(list1, 0, len(list1) - 1))
    # print(reverse_bin(list3, 0, len(list3) - 1))
    # print(list1)
    # print(getMax(list1, 0, len(list1) - 1))


# 第三题
# class Node:
#     def __init__(self, value):
#         self.parent = None
#         self.left = None
#         self.right = None
#         self.value = value


def findSuccessorNode(node):
    if node.right is not None:
        return findMostLeft(node)
    else:
        par = node.parent
        while par is not None and node.parent is not None:
            if par.left == node:
                return par.value
            else:
                node = par
                par = node.parent


def findMostLeft(node):
    if node is None:
        return
    else:
        temp = node.right
        while temp.left is not None:
            temp = temp.left
        return temp.value


# head = Node(6)
# head.left = Node(3)
# head.left.parent = head
# head.left.left = Node(1)
# head.left.left.parent = head.left
# head.left.left.right = Node(2)
# head.left.left.right.parent = head.left.left
# head.left.right = Node(4)
# head.left.right.parent = head.left
# head.left.right.right = Node(5)
# head.left.right.right.parent = head.left.right
# head.right = Node(9)
# head.right.parent = head
# head.right.left = Node(8)
# head.right.left.parent = head.right
# head.right.left.left = Node(7)
# head.right.left.left.parent = head.right.left
# head.right.right = Node(10)
# head.right.right.parent = head.right

# test = head.left.left
# print(test.value)
# print(findSuccessorNode(test))
# test = head.left.left.right
# print(test.value)
# print(findSuccessorNode(test))
# test = head.left
# print(test.value)
# print(findSuccessorNode(test))
# test = head.left.right
# print(test.value)
# print(findSuccessorNode(test))
# test = head.left.right.right
# print(test.value)
# print(findSuccessorNode(test))
# test = head
# print(test.value)
# print(findSuccessorNode(test))
# test = head.right.left.left
# print(test.value)
# print(findSuccessorNode(test))
# test = head.right.left
# print(test.value)
# print(findSuccessorNode(test))
# test = head.right
# print(test.value)
# print(findSuccessorNode(test))
# test = head.right.right
# print(test.value)
# print(findSuccessorNode(test))



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/15 16:05
# @Author  : 一条很咸很咸的咸鱼

# 题目一
import random


def question1(arr, num):
    min_scale, l = -1, 0
    for l in range(len(arr)):
        if arr[l] <= num:
            arr[l], arr[min_scale + 1] = arr[min_scale + 1], arr[l]
            min_scale += 1
    return arr


# 荷兰国旗 patition.
def helan_guoqi(arr, num):
    min_scale, max_scale, cur = -1, len(arr), 0
    while cur < max_scale:
        if arr[cur] < num:
            arr[cur], arr[min_scale + 1] = arr[min_scale + 1], arr[cur]
            min_scale += 1
            cur += 1
        elif arr[cur] > num:
            arr[cur], arr[max_scale - 1] = arr[max_scale - 1], arr[cur]
            max_scale -= 1
        elif arr[cur] == num:
            cur += 1
    return arr


# 用NetherlandsFlag改进快速排序
# 时间复杂度O(NlogN)
# 空间复杂度O(logN)
def partition_test(arr, l, r):
    less = l - 1
    more = r  # more 不能等于r+1 最后一个位置是划分值,从r-1位置开始存放大于arr[r]的值
    cur = l
    while cur < more:
        if arr[cur] < arr[r]:
            arr[cur], arr[less + 1] = arr[less + 1], arr[cur]
            less += 1
            cur += 1
        elif arr[cur] > arr[r]:
            arr[cur], arr[more - 1] = arr[more - 1], arr[cur]
            more -= 1
        else:
            cur += 1
    arr[more], arr[r] = arr[r], arr[more]  # 把划分值放在大于区域的第一个
    return less + 1, more  # 返回值为等于区域的下标


def quickSort(arr, l, r):
    if l < r:
        p1, p2 = partition_test(arr, l, r)
        quickSort(arr, l, p1 - 1)
        quickSort(arr, p2 + 1, r)


# 改进(NetherLandsFlag)再改进(随机选一个值作为划分值)快速排序
def better_quick_sort(arr, l, r):
    if l < r:
        random_value = random.randint(l, r)
        arr[r], arr[random_value] = arr[random_value], arr[r]
        p1, p2 = partition_test(arr, l, r)
        better_quick_sort(arr, l, p1 - 1)
        better_quick_sort(arr, p2 + 1, r)


# 堆排序
def heap_sort(arr):
    # 建立大根堆
    for i in range(len(arr)):
        heap_insert(arr, i)
    heapsize = len(arr) - 1
    # 堆调整
    while heapsize > 0:
        arr[0], arr[heapsize] = arr[heapsize], arr[0]
        heapsize -= 1
        heapify(arr, 0, heapsize)

# 建立大根堆
def heap_insert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        arr[index], arr[int((index - 1) / 2)] = arr[int((index - 1) / 2)], arr[index]
        index = int((index - 1) / 2)


# 建立好的大根堆中元素值变小,往下沉的过程.
def heapify(arr, index, heapsize):
    left = 2 * index + 1
    while left <= heapsize:
        if left + 1 <= heapsize:
            max_value = max(arr[left], arr[left + 1])
            max_index = left if arr[left] >= arr[left + 1] else left + 1
        else:
            max_value = arr[left]
            max_index = left
        if arr[index] >= max_value:
            break
        else:
            arr[index], arr[max_index] = arr[max_index], arr[index]
            index = max_index
            left = 2 * index + 1


# 堆排序求中位数
def median_quick(arr):
    res_left = []  # 存储最大堆中的数据
    res_right = []  # 存储最小堆中的数据
    res_left.append(arr.pop(0))
    max_value = res_left[0]# 弹出数组的第一个数加入最大堆, 返回堆顶元素
    while len(arr) > 0:
        value_arr = arr.pop(0)
        if value_arr > max_value:  # 加入最小堆的情况
            res_right.append(value_arr)
            make_min_heap(res_right)
        else:
            res_left.append(value_arr)
            max_value = make_max_heap(res_left)
        # 比较两个数组的长度
        length_max = len(res_left)
        length_min = len(res_right)
        # 最大堆中元素多于最小堆中元素时,拿出堆顶加入最小堆
        if abs(length_max - length_min) > 1 and length_max > length_min:
            res_right.append(res_left[0])
            res_left = res_left[1:]
            make_min_heap(res_right)
            heap_maxheap(res_left)
        # 最小堆中元素多于最大堆中元素时,拿出堆顶元素加入最大堆
        elif abs(length_min - length_max) > 1 and length_min > length_max:
            res_left.append(res_right[0])
            res_right = res_right[1:]
            make_max_heap(res_left)
            heap_minheap(res_right)
    if len(res_left) == len(res_right):
        return (res_left[0] + res_right[0]) / 2
    elif len(res_left) > len(res_right):
        return res_left[0]
    else:
        return res_right[0]

def heap_minheap(res_right):
    if len(res_right) >= 2:
        if res_right[0] > res_right[1]:
            res_right[0], res_right[1] = res_right[1], res_right[0]


def heap_maxheap(res_left):
    if len(res_left) >= 2:
        if res_left[0] < res_left[1]:
            res_left[0], res_left[1] = res_left[1], res_left[0]

def make_max_heap(res_left):
    index = len(res_left) - 1
    while res_left[index] > res_left[int((index - 1) / 2)]:
        res_left[index], res_left[int((index - 1) / 2)] = res_left[int((index - 1) / 2)], res_left[index]
        index = int((index - 1) / 2)
    return res_left[0]

def make_min_heap(res_right):
    index = len(res_right) - 1
    while res_right[index] < res_right[int((index - 1) / 2)]:
        res_right[index], res_right[int((index - 1) / 2)] = res_right[int((index - 1) / 2)], res_right[index]
        index = int((index - 1) / 2)
    return res_right[0]

arr_test = [2, 1, 3, 6, 0, 4]
arr_test2 = [1, 2, 3]
arr_test3 = [1]
# print(median_quick(arr_test3))
# heap_sort(arr_test)
# print(arr_test)

test1 = [5, 3, 2, 5, 68, 1, 2]
test3 = [1, 2, 2, 3, 5, 5, 68]
# num1 = 4

# heap_sort(test1)
# print(test1)
test2 = [4, 5, 545, 4, 5]
print(median_quick(test2))
num2 = 3
# heap_sort(test2)
# print(test2)
# print(question1(test1, num1))
# print(question1(test2, num2))
# print(helan_guoqi(test1, num1))
# print(helan_guoqi(test2, num2))
# quickSort(test1, 0, len(test1) - 1)
# better_quick_sort(test1, 0, len(test1) - 1)
# better_quick_sort(test2, 0, len(test2) - 1)
# print(test1)
# print(test2)
# print(question1([2, 7, 3, 6, 5], 5))
# print(helan_guoqi([2, 7, 3, 6, 5], 5))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/15 17:22
# @Author  : 一条很咸很咸的咸鱼

# 比较器
from functools import cmp_to_key


#
# class Student:
#     def __init__(self, id, age):
#         self.id = id
#         self.age = age
#
#     def __str__(self):
#         return "{}-{}".format(self.id, self.age)


# 基于id的比较器
# def compare_test(o1, o2):
#     return o1.id - o2.id
#
# stu1 = Student(1, '15')
# stu2 = Student(2, '16')
# stu3 = Student(3, '17')
# stu_list = [stu1, stu2, stu3]
# res = sorted(stu_list, key=cmp_to_key(compare_test))
# for item in res:
#     print(item)

# print(int(510/99))
# print(max(float('-inf'), 5))
# print(max(3, 5))

# list1 = [1, 2, 3, 4]
# print(list1.pop(0))
# print(list1)

# list1 = [1, 2, 3]
# print(list(reversed(list1)))
# print(list)

# small = 1
# print(not small)

# test_dict = {1: 111, 2: 2, 3: 3, 4: 4}
# print(list(test_dict.values())[0])
# str_test = '1_2_3_'
# res = str_test.split('_')[:-1]
# print(res.pop())
# print(str_test.split('_')[:-1])


# 中序遍历非递归
# def inorderTraversal(head):
#     node_list = []
#     while node_list or head:
#         if head:
#             node_list.append(head)
#             head = head.left
#         else:
#             head = node_list.pop(-1)
#             print(head.value)
#             head = head.right
#
#
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# head2 = Node(1)
# head2.left = Node(2)
# head2.right = Node(3)
# head2.right.right = Node(5)
# head2.left.left = Node(4)
#
# inorderTraversal(head2)
from random import randint

print(randint(1, 5))

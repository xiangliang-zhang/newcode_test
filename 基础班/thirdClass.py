#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/17 16:30
# @Author  : 一条很咸很咸的咸鱼

# 比较器
# 例子：定义一个学生类，对学生排序
import functools
from inspect import stack


class Student(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def __str__(self):  # 输出实例化类的对象的时候用到此函数.
        return '{},{},{}'.format(self.name, self.age, self.id)


# 年龄按照从小到大排序
def myCom_age(o1, o2):
    return o1.age - o2.age


# 先按照班级排好，再按照年龄从大到小排好
def myCom_No_age(o1, o2):
    if o1.id != o2.id:
        return o1.id - o2.id
    return o2.age - o2.age


stu1 = Student('摸鱼人生', 16, 1)
stu2 = Student('尾号9536', 18, 2)
stu3 = Student('奔跑', 12, 3)
stu4 = Student('没落', 25, 4)
arrs = [stu1, stu2, stu3, stu4]

# lambda 原理即为比较器.
# res = sorted(arrs, key=lambda x: x.age)
# for item in res:
#     print(item)

# print(max(arrs, key=lambda x: x.age))

# python3不支持比较函数，在一些接受key的函数中（例如sorted，min，max，heapq.nlargest，itertools.groupby），
# key仅仅支持一个参数，就无法实现两个参数之间的对比，采用cmp_to_key 函数，可以接受两个参数，将两个参数做处理，
# 比如做和做差，转换成一个参数，就可以应用于key关键字之后。
# 举例:
# L = [1, 2, 3, 4, 5]
# sorted(L, key=functools.cmp_to_key(lambda x, y: y - x))

# python中比较器的手动实现
# b = sorted(arrs, key=functools.cmp_to_key(myCom_age))
# for j in b:
#     print(j)
'''
奔跑,12,1
摸鱼人生,16,1
尾号9536,18,2
没落,25,2
'''
# arrs.sort(key=functools.cmp_to_key(Student.myCom_No_age))
# for i in range(len(arrs)):
#     print(arrs[i])
'''
摸鱼人生,16,1
奔跑,12,1
尾号9536,18,2
没落,25,2
'''


# 桶排序补充问题

# 返回值i所在范围----重点
# def index_state(i, max_value, min_value, length):
#     return int((i - min_value) * length / (max_value - min_value))
#
#
# def maxGap(arr):
#     if not arr or len(arr) < 2:
#         return 0
#     length = len(arr)
#     max_value = max(arr)
#     min_value = min(arr)
#     if max_value == min_value:
#         return 0
#     state = [0] * (len(arr) + 1)
#     min_state = [float('inf')] * (len(arr) + 1)
#     max_state = [float('-inf')] * (len(arr) + 1)
#     for i in arr:
#         bid = index_state(i, max_value, min_value, length)
#         min_state[bid] = min(min_state[bid], i)
#         max_state[bid] = max(max_state[bid], i)
#         state[bid] = 1
#     res = float('-inf')
#     lastMax = max_state[0]
#     for i in range(1, len(state)):
#         if state[i] == 0:
#             continue
#         res = max(res, min_state[i] - lastMax)
#         lastMax = max_state[i]
#     return res
#
# arr = [8, 7, 5, 4, 9, 11]
# arr2 = [1, 100, 3, 10000]
# arr3 = [1]
# print(maxGap(arr3))

# 第三课题目一---用数组手动实现栈

# class arr_stack:
#     arr = []
#     cur_size = 0
#
#     def __init__(self, size):
#         if size < 0:
#             raise ValueError('输入范围错误')
#         self.size = size
#
#     def peek(self):  # 获取栈顶元素
#         if self.cur_size == 0:
#             return None
#         else:
#             return self.arr[-1]
#
#     def push(self, value):
#         if self.cur_size == self.size:
#             raise Exception('范围错误')
#         self.arr.append(value)
#         self.cur_size += 1
#
#     # 出栈并没有真正的删除元素,只是index移动走了, 如果有新的元素,会覆盖
#     def pop(self):
#         if self.cur_size == 0:
#             raise Exception('范围错误')
#         temp = self.arr[-1]
#         self.cur_size -= 1
#         return temp
#
#
# test_arr = arr_stack(5)
# test_arr.push(1)
# test_arr.push(2)
# print(test_arr.peek())
# test_arr.push(3)
# test_arr.push(4)
# test_arr.push(5)
# test_arr.push(6)

# 第三课题目一----用数组手动实现队列
# class queue_arr:
#
#     def __init__(self, initsize):
#         if initsize < 0:
#             raise Exception('输入范围错误')
#         self.initsize = initsize
#         self.cur_size = 0
#         self.start = 0
#         self.end = 0
#         self.arr = []
#
#     def peek(self):
#         if self.cur_size == 0:
#             raise Exception('空数组')
#         return self.arr[self.start]
#
#     def push(self, value):
#         if self.cur_size == self.initsize:
#             raise Exception('数组满了')
#         self.arr.append(value)
#         self.cur_size += 1
#         self.end = self.end + 1 if self.end + 1 < self.initsize else 0
#
#     def pop(self):
#         if self.cur_size == 0:
#             raise Exception('数组为空')
#         self.cur_size -= 1
#         temp = self.arr[self.start]
#         self.start = self.start + 1 if self.start + 1 < self.initsize else 0
#         return temp
#
#
# queue_test = queue_arr(3)
# queue_test.push(1)
# queue_test.push(2)
# queue_test.push(3)
# queue_test.pop()
# queue_test.push(4)
# print(queue_test.peek())

# 题目二--实现特殊栈
# python中的栈可以用数组来实现
# class getMinStack():
#     data_stack = []
#     min_stack = []
#
#     def peek(self):
#         if len(self.data_stack) == 0:
#             raise Exception('栈空')
#         return self.data_stack[-1]
#
#     def push(self, value):
#         self.data_stack.append(value)
#         if len(self.min_stack) == 0:
#             self.min_stack.append(value)
#         else:
#             min_value = self.min_stack[-1]
#             self.min_stack.append(min(min_value, value))
#
#     def pop(self):
#         if len(self.data_stack) == 0:
#             raise Exception('栈空,无法弹出元素')
#         return self.data_stack.pop(-1)
#
#     def getMin(self):
#         if len(self.min_stack) == 0:
#             raise Exception('栈空,无法弹出最小值')
#         return self.min_stack.pop(-1)
#
# min_stack = getMinStack()
# min_stack.getMin()
# min_stack.pop()
# min_stack.push(5)
# min_stack.push(4)
# min_stack.push(3)
# min_stack.push(4)
# min_stack.pop()
# print(min_stack.getMin())
# print(min_stack.peek())

# 题目三--用列表实现栈
# python中没有类似java中的stack/queue,用队列来实现栈.

# class queue_arr:
#
#     # 属性定义在里面和外面的区别: 定义在里面每次实例化对象都会重新创建, 如果定义在外面,每次调用的都是同一个,不是新创建的.
#     def __init__(self):
#         self.arr = []
#         self.start = 0
#         self.end = 0
#
#     def push(self, value):
#         self.arr.append(value)
#
#     def pop(self):
#         if len(self.arr) == 0:
#             raise Exception('队列为空')
#         return self.arr.pop(0)
#
#     def peek(self):
#         if len(self.arr) == 0:
#             raise Exception('顶为空')
#         return self.arr[0]


# queue_test = queue_arr()
# queue_test.peek()
# queue_test.pop()
# queue_test.push(5)
# queue_test.push(3)
# queue_test.pop()
# print(queue_test.peek())

# 用队列来实现栈
# class stack_use_queue:
#     def __init__(self):
#         self.queue1 = queue_arr()  # 队列1
#         self.queue2 = queue_arr()  # 队列2
#
#     def push_stack(self, value):
#         self.queue1.push(value)
#
#     def pop_stack(self):
#         if len(self.queue1.arr) == 0:
#             raise Exception('栈为空, 无法出栈')
#         while len(self.queue1.arr) != 1:
#             self.queue2.push(self.queue1.pop())
#         res = self.queue1.pop()
#         self.swap_queue()
#         return res
#
#
#     def peek_stack(self):
#         if len(self.queue1.arr) == 0:
#             raise Exception('栈空,无法得到栈顶元素')
#         while len(self.queue1.arr) != 1:
#             self.queue2.push(self.queue1.pop())
#         return self.queue1.peek()
#
#     def swap_queue(self):
#         temp_queue = self.queue1
#         self.queue1 = self.queue2
#         self.queue2 = temp_queue


# queue_test = stack_use_queue()
# queue_test.peek_stack()
# queue_test.pop_stack()
# queue_test.push_stack(5)
# queue_test.push_stack(3)
# queue_test.push_stack(2)
# print(queue_test.pop_stack())
# print(queue_test.pop_stack())
# print(queue_test.pop_stack())
# print(queue_test.pop_stack())
# print(queue_test.peek_stack())

# 题目三---用栈结构实现队列
class stack_arr:
    def __init__(self):
        self.arr = []

    def push(self,value):
        self.arr.append(value)

    def pop(self):
        if len(self.arr) == 0:
            raise Exception('栈空,无法出战')
        return self.arr.pop(-1)

    def peek(self):
        if len(self.arr) == 0:
            raise Exception('栈空,无栈顶元素')
        return self.arr[-1]

# stack_test = stack_arr()
# stack_test.pop()
# stack_test.peek()
# stack_test.push(5)
# stack_test.push(3)
# stack_test.pop()
# print(stack_test.peek())

class queue_use_stack:
    def __init__(self):
        self.stack1 = stack_arr()
        self.stack2 = stack_arr()

    def push(self, value):
        self.stack1.push(value)

    def pop(self):
        if len(self.stack1.arr) == 0 and len(self.stack2.arr) == 0:
            raise Exception('队列空')
        if len(self.stack2.arr) > 0:
            return self.stack2.pop()
        else:
            while len(self.stack1.arr) > 0:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        if len(self.stack1.arr) == 0 and len(self.stack2.arr) == 0:
            raise Exception('队列空')
        if len(self.stack2.arr) > 0:
            return self.stack2.peek()
        else:
            while len(self.stack1.arr) > 0:
                self.stack2.push(self.stack1.pop())
            return self.stack2.peek()

queue_test = queue_use_stack()
# queue_test.peek()
# queue_test.pop()
queue_test.push(5)
queue_test.push(3)
print(queue_test.pop())
# print(queue_test.peek())
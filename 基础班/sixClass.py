#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/9 15:58
# @Author  : 一条很咸很咸的咸鱼

# 题目二--设计RandomPool结构
from random import randint


class RandomPool:
    def __init__(self):
        self.hashmap1 = {}  # key : index
        self.hashmap2 = {}  # index : key
        self.size = 0

    def insert(self, key):
        if key not in self.hashmap1.keys():
            self.size += 1
            self.hashmap1[key] = self.size
            self.hashmap2[self.size] = key

    def getRandom(self):
        if self.size == 0:
            return None
        temp_int = randint(1, self.size)
        return self.hashmap2[temp_int]

    def delete(self, key):
        if key in self.hashmap1.keys():
            temp_value = self.hashmap1[key]  # 获取index
            last_key = self.hashmap2[self.size]
            # hashmap1中删除并增加
            del self.hashmap1[key]  # 删除hashmap1元素
            self.hashmap1[last_key] = temp_value
            # hashmap2中删除增加
            self.hashmap2[temp_value] = self.hashmap2[self.size]
            del self.hashmap2[self.size]  # 删除hashmap2最后一个元素
            self.size -= 1


test = RandomPool()
test.insert(1)
test.insert(2)
test.insert(3)
test.insert(4)
test.insert(5)
test.delete(2)
test.delete(1)
test.delete(1)
for i in range(100):
    print(test.getRandom(), end=' ')
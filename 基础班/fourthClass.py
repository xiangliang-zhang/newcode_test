#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/7/21 15:45
# @Author  : 一条很咸很咸的咸鱼

# 题目四:猫狗队列
class Pet:
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        super().__init__('dog')


class Cat(Pet):
    def __init__(self):
        super().__init__('cat')


class PetEnterQueue:

    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def getPet(self):
        return self.pet

    def getCount(self):
        return self.count

    def getEnterType(self):
        return self.pet.getPetType()


class DogCatQueue:

    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.count = 0

    def add(self, pet):
        if pet.getPetType() == 'dog':
            self.count += 1
            temp = PetEnterQueue(pet, self.count)
            self.dog_queue.append(temp)
        elif pet.getPetType() == 'cat':
            self.count += 1
            temp = PetEnterQueue(pet, self.count)
            self.cat_queue.append(temp)
        else:
            raise Exception('not cat or dog')

    def pollAll(self):
        if len(self.cat_queue) == 0 and len(self.dog_queue) == 0:
            raise Exception('cat and dog queue are none!')
        elif len(self.cat_queue) == 0:
            return self.dog_queue.pop(0).getPet()
        elif len(self.dog_queue) == 0:
            return self.cat_queue.pop(0).getPet()
        else:
            if self.dog_queue[0].getCount() < self.cat_queue[0].getCount():
                return self.dog_queue.pop(0).getPet()
            else:
                return self.cat_queue.pop(0).getPet()

    def pollDog(self):
        if len(self.dog_queue) != 0:
            return self.dog_queue.pop(0).getPet()

    def pollCat(self):
        if len(self.cat_queue) != 0:
            return self.cat_queue.pop(0).getPet()

    def isEmpty(self):
        if len(self.dog_queue) == 0 and len(self.cat_queue) == 0:
            return True
        return False

    def isDogEmpty(self):
        if len(self.dog_queue) == 0:
            return True
        return False

    def isCatEmpty(self):
        if len(self.cat_queue) == 0:
            return True
        return False


# dog1 = Dog()
# cat1 = Cat()
# dog2 = Dog()
# cat2 = Cat()
# dog_cat_queuen = DogCatQueue()
# dog_cat_queuen.add(dog1)
# dog_cat_queuen.add(cat1)
# dog_cat_queuen.add(dog2)
# dog_cat_queuen.add(cat2)
# print(dog_cat_queuen.isCatEmpty())
# print(dog_cat_queuen.isDogEmpty())
# print(dog_cat_queuen.pollCat().getPetType())
# print(dog_cat_queuen.pollDog().getPetType())
# while not dog_cat_queuen.isEmpty():
#     print(dog_cat_queuen.pollAll().getPetType())
# print(test1.getCount())
# print(test1.getPet())
# print(dog1.getPetType())
# print(cat1.getPetType())
# dog_cat_queuen = DogCatQueue()
# dog_cat_queuen.add()


# 题目五:转圈打印矩阵
# def rotate_print_Matrix(arr):
#     lt_x = 0
#     lt_y = 0
#     rb_x = len(arr) - 1
#     rb_y = len(arr[0]) - 1
#     while lt_x <= rb_x and lt_y <= rb_y:
#         operate_matrix(arr, lt_x, lt_y, rb_x, rb_y)
#         lt_x += 1
#         lt_y += 1
#         rb_x -= 1
#         rb_y -= 1


# def operate_matrix(arr, lt_x, lt_y, rb_x, rb_y):
#     if lt_x == rb_x:  # 一行
#        for i in range(lt_y, rb_y + 1):
#            print(arr[lt_x][i], end=' ')
#     elif lt_y == rb_y:  # 一列
#         for i in range(lt_x, rb_x + 1):
#             print(arr[i][lt_y])
#     else:
#         cury = lt_y
#         curx = lt_x
#         while cury < rb_y:
#             print(arr[curx][cury], end=' ')
#             cury += 1
#         while curx < rb_x:
#             print(arr[curx][cury], end=' ')
#             curx += 1
#         while cury > lt_y:
#             print(arr[curx][cury], end=' ')
#             cury -= 1
#         while curx > lt_x:
#             print(arr[curx][cury], end=' ')
#             curx -= 1

# arr1 = [[1, 2, 3, 4]]
# arr2 = [[1], [2], [3], [4]]
# arr3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# rotate_print_Matrix(arr3)

# 题目六---旋转正方形矩阵
# def rotate_square_matrix(arr):
#     lt_x = 0
#     lt_y = 0
#     rb_x = len(arr) - 1
#     rb_y = len(arr[0]) - 1
#     while lt_x < rb_x:
#         operate_square(arr, lt_x, lt_y, rb_x, rb_y)
#         lt_x += 1
#         lt_y += 1
#         rb_x -= 1
#         rb_y -= 1
#     print_format(arr)
#
#
# def operate_square(arr, lt_x, lt_y, rb_x, rb_y):
#     for i in range(lt_y, rb_y):
#         temp = arr[lt_x][lt_y + i]  # 注意点 lt_y + i, 不是 i, 如果不加, 最外层不会有问题, 内层会出现问题
#         arr[lt_x][lt_y + i] = arr[rb_x - i][lt_y]
#         arr[rb_x - i][lt_y] = arr[rb_x][rb_y - i]
#         arr[rb_x][rb_y - i] = arr[lt_x + i][rb_y]
#         arr[lt_x + i][rb_y] = temp
#
#
# def print_format(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             print(arr[i][j], end=' ')
#         print()
#
#
# arr3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# arr4 = [[6, 7], [10, 11]]
# rotate_square_matrix(arr3)

# 题目七 --- 反转单项链表
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
# def reverse_node_list(head):
#     pre = None
#     while head:
#         next_node = head.next
#         head.next = pre
#         pre = head
#         head = next_node
#     return pre
#
# class double_linked_node_list:
#     def __init__(self, value):
#         self.value = value
#         self.before = None
#         self.next = None
#
# def reverse_double_linked_list(head):
#     pre = None
#     while head:
#         # 只需要移动当前节点的next, before, 不需要动其他节点的
#         next_node = head.next
#         head.next = pre
#         head.before = next_node
#         pre = head
#         head = next_node
#     return pre

# 题目八----之字形打印.
# def zigzag_matrix(arr):
#     a_row = 0
#     a_column = 0
#     b_row = 0
#     b_column = 0
#     length_row = len(arr) - 1
#     length_column = len(arr[0]) - 1
#     tag = True
#     while a_row < len(arr):
#         output_matrix(arr, a_row, a_column, b_row, b_column, tag)
#         a_row = a_row + 1 if a_column == length_column else a_row
#         a_column = a_column + 1 if a_column < length_column else a_column
#         b_column = b_column + 1 if b_row == length_row else b_column
#         b_row = b_row + 1 if b_row < length_row else b_row
#         tag = not tag
#
#
# def output_matrix(arr, a_row, a_column, b_row, b_column, tag):
#     if tag:
#         while a_row <= b_row:
#         # while a_row <= b_row and a_column >= b_column:
#             print(arr[b_row][b_column], end=' ')
#             b_row -= 1
#             b_column += 1
#     elif not tag:
#         while b_row >= a_row:
#         # while a_row <= b_row and a_column >= b_column:
#             print(arr[a_row][a_column], end=' ')
#             a_row += 1
#             a_column -= 1
#
#
arr_test = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


# zigzag_matrix(arr_test)

# 题目九---在行列排好序的矩阵中查找元素.
# def find_item(arr, x):
#     init_x = 0
#     init_y = len(arr[0]) - 1
#     while init_x < len(arr) and init_y >= 0:
#         if arr[init_x][init_y] == x:
#             return True
#         if arr[init_x][init_y] > x:
#             init_y -= 1
#         else:
#             init_x += 1
#     return False
#
# print(find_item(arr_test, 1))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(7)
node2 = Node(9)
node3 = Node(1)
node4 = Node(8)
node5 = Node(5)
node6 = Node(2)
node7 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
head1 = node1


# node6 = Node(4)
# node7 = Node(5)
# node8 = Node(6)
# node9 = Node(7)
# node10 = Node(8)
# node6.next = node7
# node7.next = node8
# node8.next = node9
# node9.next = node10
# head2 = node6

#  题目十---打印有序链表的公共部分
# def same_part(head1, head2):
#     res = []
#     while head1 and head2:
#         if head1.value == head2.value:
#             res.append(head1.value)
#             head1 = head1.next
#             head2 = head2.next
#         elif head1.value < head2.value:
#             head1 = head1.next
#         else:
#             head2 = head2.next
#     return res
#
# print(same_part(head1, head2))

# 题目十一---判断链表是否是回文结构.
# 方法一:空间复杂度O(N)
# def is_plalindrome(head):
#     list_res = []
#     while head:
#         list_res.append(head.value)
#         head = head.next
#     return list_res == list(reversed(list_res))
#
# print(is_plalindrome(head2))

# 方法二:空间复杂度O(N/2)
# def is_palindrome(head):
#     quick = head
#     slow = head
#     res_right_part = []
#     while quick.next and quick.next.next:
#         quick = quick.next.next
#         slow = slow.next
#     slow = slow.next
#     while slow:
#         res_right_part.append(slow.value)
#         slow = slow.next
#     temp = head
#     while res_right_part:
#         if temp.value == res_right_part.pop(-1):
#             temp = temp.next
#         else:
#             return False
#     return True
#
# print(is_palindrome(head1))

# 方法三: 空间复杂度O(1) 改变链表结构
# def is_palindrome(head):
#     quick = head
#     slow = head
#     while quick.next and quick.next.next:
#         quick = quick.next.next
#         slow = slow.next
#     cur = slow.next
#     slow.next = None
#     pre = slow
#     while cur:
#         cur_next = cur.next
#         cur.next = pre
#         pre = cur
#         cur = cur_next
#     left = head
#     right = pre
#     res = 0
#     while left and right:
#         if left.value != right.value:
#             res = 1
#             break
#         else:
#             left = left.next
#             right = right.next
#     head_right = pre
#     pre = None
#     while head_right:
#         head_next = head_right.next
#         head.next = pre
#         pre = head_right
#         head_right = head_next
#     slow.next = pre
#     if res == 1:
#         return False
#     else:
#         return True
#
# print(is_palindrome(head1))

# 题目十二---单向链表的荷兰国旗问题
# 方法一:荷兰国旗 空间复杂度O(N)
# def small_equal_bigger(head, num):
#     temp = head
#     res = []
#     while temp:
#         res.append(temp)
#         temp = temp.next
#     less, cur, more = -1, 0, len(res)
#     while cur < more:
#         if res[cur].value == num:
#             cur += 1
#         elif res[cur].value < num:
#             less += 1
#             res[cur], res[less] = res[less], res[cur]
#             cur += 1
#         else:
#             more -= 1
#             res[cur], res[more] = res[more], res[cur]
#     head = res[0]
#     temp = head
#     for i in range(1, len(res)):
#         temp.next = res[i]
#         temp = temp.next
#     return head
#
#
# small_equal_bigger(head1, 3)

# 方法二---重构链表 空间复杂度O(1)
# def small_euqal_bigger(head, num):
#     small = None
#     equal = None
#     bigger = None
#     end_small = None
#     end_equal = None
#     end_bigger = None
#     # 第一次遍历,找出第一个小于/等于/大于的节点.
#     while head:
#         temp = head.next
#         head.next = None
#         if head.value < num:
#             if not small:
#                 small = head
#                 end_small = head
#             else:
#                 end_small.next = head
#                 end_small = head
#         elif head.value == num:
#             if not equal:
#                 equal = head
#                 end_equal = head
#             else:
#                 end_equal.next = head
#                 end_equal = head
#         elif head.value > num:
#             if not bigger:
#                 bigger = head
#                 end_bigger = head
#             else:
#                 end_bigger.next = head
#                 end_bigger = head
#         head = temp
# end_samll/end_equal/end_bigger判空
# if end_small:  # 如果small不为空, 此种情况下肯定返回small
#     if equal:  # 如果small不为空且equal不为空
#         end_small.next = equal
#         if bigger:  # 如果small不为空且equal不为空且bigger不为空
#             end_equal.next = bigger
#     elif equal is None:
#         if bigger:
#             end_small.next = bigger
#     return small
# elif end_small is None:
#     if equal:
#         if bigger:
#             end_equal.next = bigger
#         return equal
#     else:
#         return bigger


# res = small_euqal_bigger(head1, 10)
# while res:
#     print(res.value, end=' ')
#     res = res.next


# 题目十三--复制含有特殊指针的链表
# class sp_listNode:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.rand = None


# 方法一:哈希表辅助实现
# 分析:时间复杂度O(N) 空间复杂度O(N)
# def copy_special_list(list_head):
#     hash_list = {}
#     while list_head:
#         new_node = sp_listNode(list_head.value)
#         hash_list[list_head] = new_node
#         list_head = list_head.next
#     for init_item, copy_item in hash_list.items():
#         if init_item.next:
#             copy_item.next = hash_list[init_item.next]
#         else:
#             copy_item.next = None
#         if init_item.rand:
#             copy_item.rand = hash_list[init_item.rand]
#         else:
#             copy_item.rand = None
#     res = list(hash_list.values())[0]
#     return list(hash_list.values())[0]

# 方法二:利用链表结构实现哈希表原理(不适用额外数据结构)
# def copy_special_list2(list_head):
#     temp_head = list_head
#     while temp_head:
#         temp_node = sp_listNode(temp_head.value)
#         temp_node.next = temp_head.next
#         temp_head.next = temp_node
#         temp_head = temp_head.next.next
#     origin_pointer, copy_pointer = list_head, list_head.next
#     while copy_pointer.next:
#         copy_pointer.rand = origin_pointer.rand.next
#         origin_pointer = origin_pointer.next.next
#         copy_pointer = copy_pointer.next.next
#     head1, head2 = list_head, list_head.next
#     temp_pointer2 = list_head.next
#     while temp_pointer2.next:
#         head1.next = temp_pointer2.next
#         head1 = temp_pointer2.next
#         temp_pointer2.next = head1.next
#         temp_pointer2 = head1.next
#     res = head2
#     return head2


# 创建测试用例
# sp_node1 = sp_listNode(1)
# sp_node2 = sp_listNode(2)
# sp_node3 = sp_listNode(3)
# sp_node1.next = sp_node2
# sp_node2.next = sp_node3
# sp_node1.rand = sp_node3
# sp_node2.rand = sp_node1
#
# print(copy_special_list(sp_node1))
# print(copy_special_list2(sp_node1))

# 第十四题
class node:
    def __init__(self, value):
        self.value = value
        self.next = None


# 获取链表循环开始的节点
def getloop(head):
    slow = head
    fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            fast = head
            while fast:
                fast = fast.next
                slow = slow.next
                if slow == fast:
                    return slow
    return None


# 无环情况下获取相交的第一个节点
def getNodeNoLoop(head1, head2):
    cur_head1 = head1
    cur_head2 = head2
    length1 = 0
    length2 = 0
    while cur_head1:
        length1 += 1
        if cur_head1.next == None:
            end1 = cur_head1
        cur_head1 = cur_head1.next
    while cur_head2:
        length2 += 1
        if cur_head2.next == None:
            end2 = cur_head2
        cur_head2 = cur_head2.next
    if end1 != end2:
        return None
    else:
        dif = abs(length2 - length1)
    temp_head1 = head1
    temp_head2 = head2
    if length1 >= length2:
        for i in range(dif):
            temp_head1 = temp_head1.next
        while temp_head1:
            if temp_head1 == temp_head2:
                return temp_head1
            else:
                temp_head1 = temp_head1.next
                temp_head2 = temp_head2.next
    else:
        for i in range(dif):
            temp_head2 = temp_head2.next
        while temp_head1:
            if temp_head1 == temp_head2:
                return temp_head1
            else:
                temp_head1 = temp_head1.next
                temp_head2 = temp_head2.next


# 有环情况下获取相交的第一个交点
def getNodeLoop(head1, head2, loop1, loop2):
    if loop1 == loop2:
        length1 = 0
        length2 = 0
        cur_head1 = head1
        cur_head2 = head2
        while cur_head1:
            length1 += 1
            if cur_head1.next == loop1:
                end1 = cur_head1
                break
            cur_head1 = cur_head1.next
        while cur_head2:
            length2 += 1
            if cur_head2.next == loop2:
                end2 = cur_head2
                break
            cur_head2 = cur_head2.next
        dif = abs(length1 - length2)
        temp_head1 = head1
        temp_head2 = head2
        if length1 >= length2:
            for i in range(dif):
                temp_head1 = temp_head1.next
            while temp_head1:
                if temp_head1 == temp_head2:
                    return temp_head1
                else:
                    temp_head1 = temp_head1.next
                    temp_head2 = temp_head2.next
        else:
            for i in range(dif):
                temp_head2 = temp_head2.next
            while temp_head2:
                if temp_head1 == temp_head2:
                    return temp_head2
                else:
                    temp_head1 = temp_head1.next
                    temp_head2 = temp_head2.next
    else:
        cur_loop1 = loop1.next
        while cur_loop1 != loop1:
            if cur_loop1 == loop2:
                return loop1
            cur_loop1 = cur_loop1.next
        return None

def findFirstIntersectNode(head1, head2):
    loop1 = getloop(head1)
    loop2 = getloop(head2)
    # 链表1和链表2中都无环
    if loop1 == None and loop2 == None:
        return getNodeNoLoop(head1, head2).value
    elif loop1 != None and loop2 != None:
        return getNodeLoop(head1, head2, loop1, loop2).value
    else:
        return None


# 测试实例
# 1->2->3->4->5->6->7->null
test_head1 = Node(1)
test_head1.next = Node(2)
test_head1.next.next = Node(3)
test_head1.next.next.next = Node(4)
test_head1.next.next.next.next = Node(5)
test_head1.next.next.next.next.next = Node(6)
test_head1.next.next.next.next.next.next = Node(7)

# 0->9->8->6->7->null
test_head2 = Node(0)
test_head2.next = Node(9)
test_head2.next.next = Node(8)
test_head2.next.next.next = test_head1.next.next.next.next.next
# 两个链表都无环的情况
# print(findFirstIntersectNode(test_head1, test_head2))

# 1->2->3->4->5->6->7->4->5->6->7....
test_head3 = Node(1)
test_head3.next = Node(2)
test_head3.next.next = Node(3)
test_head3.next.next.next = Node(4)
test_head3.next.next.next.next = Node(5)
test_head3.next.next.next.next.next = Node(6)
test_head3.next.next.next.next.next.next = Node(7)
test_head3.next.next.next.next.next.next.next = test_head3.next.next.next


# 0->9->8->2
test_head4 = Node(0)
test_head4.next = Node(9)
test_head4.next.next = Node(8)
test_head4.next.next.next = test_head3.next
# 两个链表都有环(2)
# print(findFirstIntersectNode(test_head3, test_head4))

# 0->9->8->6->7
test_head5 = Node(0)
test_head5.next = Node(9)
test_head5.next.next = Node(8)
test_head5.next.next.next = test_head3.next.next.next.next.next
# 两个链表都有环(3)
print(findFirstIntersectNode(test_head3, test_head5))


# print(getloop(test_head1))
# print(getloop(test_head2))

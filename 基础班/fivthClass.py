#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2020/8/3 22:22
# @Author  : 一条很咸很咸的咸鱼

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# 递归先序遍历
def preTravelsalRecursion(head):
    if head is None:
        return
    print(head.value)
    preTravelsalRecursion(head.left)
    preTravelsalRecursion(head.right)


# 递归中序遍历
def inTravelsalRecursion(head):
    if head is None:
        return
    inTravelsalRecursion(head.left)
    print(head.value)
    inTravelsalRecursion(head.right)


# 递归后序遍历
def posTravelsalRecursion(head):
    if head is None:
        return
    posTravelsalRecursion(head.left)
    posTravelsalRecursion(head.right)
    print(head.value)


# 非递归先序遍历
def preTravelsal(head):
    node_stack = [head]
    while node_stack:
        res = node_stack.pop(-1)
        if res is not None:
            print(res.value)
            node_stack.append(res.right)
            node_stack.append(res.left)


# 非递归后续遍历
def posTravelsal(head):
    node_stack = [head]
    res = []
    while node_stack:
        temp = node_stack.pop(-1)
        if temp is not None:
            res.append(temp.value)
            node_stack.append(temp.left)
            node_stack.append(temp.right)
    return list(reversed(res))


# 非递归中序遍历
def inTravelsal(head):
    node_stack = []
    while node_stack or head:
        if head:
            node_stack.append(head)
            head = head.left
        else:
            head = node_stack.pop(-1)
            print(head.value)
            head = head.right


# head_test = Node(1)
# head_test.left = Node(2)
# head_test.left.left = Node(4)
# head_test.left.right = Node(5)
# head_test.right = Node(3)
# head_test.right.left = Node(6)
# head_test.right.right = Node(7)
# preTravelsalRecursion(head_test)
# inTravelsalRecursion(head_test)
# posTravelsalRecursion(head_test)
# preTravelsal(head_test)
# print(posTravelsal(head_test))
# print(inTravelsal(head_test))


# 第四题: 序列化与反序列化
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 先序序列化
def serializeByPre(head):
    if head is None:
        return '#_'
    else:
        res = str(head.value) + '_'
        res += serializeByPre(head.left)
        res += serializeByPre(head.right)
        return res


# 先序反序列化
def deserializerByPre(res):
    res = res.split('_')[:-1]
    return process_res_pre(res)


def process_res_pre(res):
    value = res.pop(0)
    if value == '#':
        return None
    head = Node(value)
    head.left = process_res_pre(res)
    head.right = process_res_pre(res)
    return head


# 中序序列化
def serializerByIn(head):
    if head is None:
        return '#_'
    res = ''
    res += serializerByIn(head.left)
    res += str(head.value) + "_"
    res += serializerByIn(head.right)
    return res


# 中序反序列化(不会)
# 中序遍历得到的二叉树不唯一,不能保证反序列化的二叉树为原来的树.
def process_res_in(res):
    value = res.pop(0)
    if value == '#':
        return None
    head = Node


def deserializerByIn(res):
    res = res.split('_')[:-1]
    process_res_in(res)


# 后序序列化
def serializerByPos(head):
    if head is None:
        return '#_'
    res = ''
    res += serializerByPos(head.left)
    res += serializerByPos(head.right)
    res += str(head.value) + "_"
    return res


# 后序反序列化(不会)
def deserializerByPos(res):
    pass


# 层次遍历序列化
def serializerByLevel(head):
    if head is None:
        return '#_'
    res = str(head.value) + '_'
    queue_list = [head]
    while queue_list:
        head = queue_list.pop(0)
        if head.left is not None:
            res += str(head.left.value) + '_'
            queue_list.append(head.left)
        else:
            res += "#_"
        if head.right is not None:
            res += str(head.right.value) + '_'
            queue_list.append(head.right)
        else:
            res += '#_'

    return res


# 层次遍历反序列化
def generateNode(val):
    if val == '#':
        return
    return Node(int(val))


def deserializerByLevel(res):
    res = res.split('_')[:-1]
    index = 0
    head = generateNode(res[index])
    index += 1
    queue_list = [head] if head is not None else []
    while len(queue_list) > 0:
        node = queue_list.pop(0)
        node.left = generateNode(res[index])
        index += 1
        node.right = generateNode(res[index])
        index += 1
        if node.left is not None:
            queue_list.append(node.left)
        if node.right is not None:
            queue_list.append(node.right)

    return head


# 题目六--判断平衡二叉树
def process_tree(head):
    # 1.base case
    if head is None:
        return [True, 0]
    # 2.判断左树
    leftData = process_tree(head.left)
    if not leftData[0]:
        return [False, 0]
    # 3.判断右树
    rightData = process_tree(head.right)
    if not rightData:
        return [False, 0]
    # 4.判断整体
    if abs(leftData[1] - rightData[1]) > 1:
        return [False, 0]
    return [True, max(leftData[1], rightData[1]) + 1]


def isBalanceBinaryTree(head):
    return process_tree(head)[0]


# 题目七--判断一棵树是否是搜索二叉树, 要么为空,要么左子树小,右子树大.
def isBalanceSearchTree(head):
    if head is None:
        return True
    return inorderTraversal2(head)


# 中序遍历非递归
# 额外存储空间
def inorderTraversal(head):
    node_stack = []
    res = []
    while node_stack or head:
        if head:
            node_stack.append(head)
            head = head.left
        else:
            head = node_stack.pop(-1)
            res.append(head.value)
            head = head.right
    print(res)
    return res == sorted(res)


def inorderTraversal2(head):
    node_stack = []
    past = float('-inf')
    while node_stack or head:
        if head:
            node_stack.append(head)
            head = head.left
        else:
            head = node_stack.pop(-1)
            cur_value = head.value
            if cur_value < past:
                return False
            past = cur_value
            head = head.right
    return True


# 判断一棵树是否是完全二叉树
# 层次遍历
def isCompleteTree(head):
    if head is None:
        return True
    node_stack = [head]
    leaf = False
    while node_stack:
        head = node_stack.pop(0)
        if head.right is not None and head.left is None:  # 右孩子不空 左孩子空
            return False
        if leaf and (head.right is not None or head.left is not None):  # 已经是叶节点, 但还有孩子的
            return False
        if head.left:
            node_stack.append(head.left)
        if head.right:
            node_stack.append(head.right)
        if head.left is None or head.right is None:  # 只要有节点的孩子为空,那么后面都为叶节点.
            leaf = True
    return True


# 计算完全二叉树的节点个数
def completeTreeNodeNum(head):
    if head is None:
        return 0
    return bs(head, 1, mostLeftLevel(head, 1))


# level:计算完全二叉树的深度
def mostLeftLevel(node, level):
    """
    给定任意位置节点,计算完全二叉树的深度.
    :param node:
    :param level:
    :return:
    """
    while node is not None:
        level += 1
        node = node.left
    return level - 1


# node: 当前节点
# l:当前节点的深度
# h:当前二叉树的深度 h总 固定值
def bs(node, l, h):
    if l == h:  # 以node为头,在l层, 且l=h, 那么节点个数只有一个, node为叶节点, 以叶节点为头的子树的节点个数为1.
        return 1
    if mostLeftLevel(node.right, l + 1) == h:  # 节点左子树为完全二叉树情况.
        return 2 ** (h - l) + bs(node.right, l + 1, h)
    else:  # 节点右子树为完全二叉树
        return 2 ** (h - l - 1) + bs(node.left, l + 1, h)


# head = None
head2 = Node(1)
head2.left = Node(2)
head2.right = Node(3)
head2.right.right = Node(5)
head2.left.left = Node(4)

# 先序序列化与反序列化结果
# print(serializeByPre(head2))
# temp = serializeByPre(head2)
# res = deserializerByPre(temp)
# print(deserializerByPre(temp))

# 中序序列化与反序列化结果(未完成)
# print(serializerByIn(head2))
# print(serializerByPos(head2))

# 层次遍历序列化与反序列化结果
# print(serializerByLevel(head2))
# temp = serializerByLevel(head2)
# print(deserializerByLevel(temp))

# 判断是否是平衡二叉树
# print(isBalanceBinaryTree(head2))

# 判断是否是搜索二叉树结果
# head = Node(3)
# head.left = Node(2)
# head.right = Node(4)
# head.right.right = Node(5)
# head.left.left = Node(1)
# print(isBalanceSearchTree(head))


# 计算完全二叉树的节点个数结果
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.left = Node(4)
head.left.right = Node(5)
head.right.left = Node(6)
head.right.right = Node(6)
# print(completeTreeNodeNum(head))

# 判断是否是完全二叉树
# print(isCompleteTree(head))


# 折纸问题
# 折一次, 1DOWN
# 折两次: 2DOWN 1DOWN 2UP
# 折三次: 3DOWN 2DOWN 3UP 1DOWN 3DOWN 2UP 3UP
# 每折一次， 上一次的节点基础上 左边多出一个DOWN 右边多出一个UP。
# 中序遍历这个二叉树,即为结果.
def printProcess(i, N, down):
    if i > N:  # 节点为空
        return
    printProcess(i + 1, N, True)  # 左子树
    if down:  # 访问当前节点
        print('down')
    else:
        print('up')
    printProcess(i+1, N, False)  # 右子树


def printAllFolds(N):
    printProcess(1, N, True)

printAllFolds(3)
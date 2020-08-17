from 中级班.第一章.class1_1 import Node

# 带头尾节点的双向链表结构
class NodeDoubleLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.before = self.head

    def addNode(self, node):
        if node.value == None:
            return
        else:
            self.tail.before.next = node
            node.before = self.tail.before
            self.tail.before = node
            node.next = self.tail

    def removeHead(self):
        if self.head.next == self.tail:
            return
        else:
            self.head.next = self.head.next.next
            self.head.next.before = self.head



    def moveNodetoTail(self, node):
        if self.tail.before == node:
            return
        else:
            node.before.next = node.next
            node.next.before = node.before
            node.next = self.tail
            node.before = self.tail.before
            self.tail.before.next = node
            self.tail.before = node

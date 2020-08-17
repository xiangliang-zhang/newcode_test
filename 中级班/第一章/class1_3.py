from 中级班.第一章.class1_2 import NodeDoubleLinkedList
from 中级班.第一章.class1_1 import Node


class MyCache:
    def __init__(self, k):
        if k < 1:
            # print('should be more than 0')  # 存在问题,怎么结束程序
            raise KeyError('k should be more than 0')
        else:
            self.k = k
            self.cache_find_value = {}  # key为data[0] value为节点地址
            self.cache_find_index = {}  # key为节点位置 value为data[0]
            self.nodedoublelinkedlist = NodeDoubleLinkedList()

    def set(self, data):
        if self.nodedoublelinkedlist.head.next == self.nodedoublelinkedlist.tail:
            node = Node(data)
            self.nodedoublelinkedlist.addNode(node)
            self.cache_find_index[data[0]] = self.nodedoublelinkedlist.head.next
            self.cache_find_value[self.nodedoublelinkedlist.head.next] = data[0]
        elif data[0] in self.cache_find_index:
            self.cache_find_index[data[0]].value = data  # 不考虑同key插入时,value的值都进行覆盖
            self.nodedoublelinkedlist.moveNodetoTail(self.cache_find_index[data[0]])
        else:
            self.nodedoublelinkedlist.addNode(Node(data))
            self.cache_find_index[data[0]] = self.nodedoublelinkedlist.tail.before
            self.cache_find_value[self.nodedoublelinkedlist.tail.before] = data[0]
            if len(self.cache_find_index) > self.k:
                self.remove_data()
                self.nodedoublelinkedlist.removeHead()



    def get(self, data):
        if data in self.cache_find_index:
            node = self.cache_find_index[data]
            self.nodedoublelinkedlist.moveNodetoTail(node)
            return (self.cache_find_index[data].value)[1]
        return


    def remove_data(self):
        value = self.nodedoublelinkedlist.head.next
        key = self.cache_find_value[value]
        del self.cache_find_index[key]
        del self.cache_find_value[value]


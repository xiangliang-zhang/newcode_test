class unionFindSet:
    def __init__(self, data_list):  # 默认传入参数为要处理的列表
        # 初始化两个字典,一个保存节点的父节点,另外一个保存父节点的大小
        self.father_dict = {}
        self.size_dict = {}

        # 字典初始化,将节点的父节点设为自身,size设为1
        for node in data_list:
            self.father_dict[node] = node  # 初始情况下,每个元素为一个集合
            self.size_dict[node] = 1  # 每个元素为一个集合,当然每个集合的长度都为1.

    # 查找父节点  递归方式查找
    # 在查找父节点的时候,顺便把当前节点移动到父节点上面.
    def find_head(self, node):
        father = self.father_dict[node]
        if node != father:
            father = self.find_head(father)
        # self.father_dict[node] = father
        return father

    def is_same_set(self, a, b):
        # 查看两个节点是否在一个集合里面.
        return self.find_head(a) == self.find_head(b)

    def union(self, a, b):
        # 将两个集合合并在一起
        if a is None or b is None:
            return
        a_head = self.find_head(a)
        b_head = self.find_head(b)

        if a_head != b_head:
            a_set_size = self.size_dict[a_head]  # 得到a集合的大小
            b_set_size = self.size_dict[b_head]  # 得到b集合的大小
            if a_set_size >= b_set_size:  # 将b集合合并到a集合中
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:  # 将a集合合并到b集合中
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size
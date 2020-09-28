#! _*_ encoding=utf-8 _*_

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = '{%d,%d}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%d,%d}' % (self.key, self.value)
        return val


class DoubleNodeList:
    def __init__(self, capacity=0xffff):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def __add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1

    def __add_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1

    # default remove tail
    def __remove(self, node):
        if not node:
            node = self.tail
        if self.head == node:
            self.__del_head()
        elif self.tail == node:
            self.__del_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
        node.prev = node.next = None
        return node

    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            node.next.prev = None
            self.head = node.next
        else:
            self.head = self.tail = None
        self.size -= 1
        return node;

    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.prev:
            node.prev.next = None
            self.tail = node.prev
        else:
            self.head = self.tail = None
        self.size -= 1
        return node

    def __empty_list(self):
        self.head = self.tail = None

    def pop(self):
        return self.__del_head()

    def append(self, node=None):
        return self.__add_tail(node)

    def append_front(self, node):
        return self.__add_head(node)

    def remove(self, node=None):
        return self.__remove(node)

    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        print(line)


if __name__ == '__main__':
    l = DoubleNodeList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)

    l.append(nodes[0])
    l.print()
    l.append(nodes[1])
    l.print()
    l.pop()
    l.print()
    l.append(nodes[2])
    l.print()
    l.append_front(nodes[3])
    l.print()
    l.append(nodes[4])
    l.print()
    l.remove(nodes[2])
    l.print()
    l.remove()
    l.print()




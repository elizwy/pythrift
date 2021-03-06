from computer_principle.node.DoubleLinkedList import *


class LRUCache(object):

    def __init__(self, capacity):
        self.map = {}
        self.list = DoubleNodeList(capacity)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.list.remove(node)
        self.list.append_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
            self.map[key] = node
        else:
            node = Node(key, value)
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2);
    cache.put(2, 2)
    cache.print()
    cache.put(1, 1)
    cache.print()
    cache.put(3, 3)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()

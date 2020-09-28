from computer_principle.node.DoubleLinkedList import *


class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 1
        super(LFUNode, self).__init__(key, value)


class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity;
        self.map = {}
        self.freq_map = {}
        self.size = 0

    def __update_freq(self, node):
        freq = node.freq
        # delete
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
        # update
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleNodeList()
        self.freq_map[freq].append(node)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__update_freq(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.map[key] = node
            self.__update_freq(node)
        else:
            if self.size == self.capacity:
                freq = min(self.freq_map)
                self.freq_map[freq].remove()
            node = LFUNode(key, value)
            self.map[key] = node
            if node.freq not in self.freq_map:
                self.freq_map[node.freq] = DoubleNodeList()
            self.freq_map[node.freq].append(node)
            self.size += 1

    def print(self):
        for k, v in self.freq_map.items():
            print('Freq=%s' % k)
            self.freq_map[k].print()
        print('******************')
        print()


if __name__ == '__main__':
    cache = LFUCache(4)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3, 3)
    cache.print()
    print(cache.get(2))
    cache.print()
    cache.put(4, 4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()

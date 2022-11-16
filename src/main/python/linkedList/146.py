#
#  请你设计并实现一个满足
#  LRU (最近最少使用) 缓存 约束的数据结构。
#
#
#
#  实现
#  LRUCache 类：
#
#
#
#
#
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
#
#
#
#
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
#  示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
#  提示：
#
#
#  1 <= capacity <= 3000
#  0 <= key <= 10000
#  0 <= value <= 10⁵
#  最多调用 2 * 10⁵ 次 get 和 put
#
#
#  Related Topics 设计 哈希表 链表 双向链表 👍 2467 👎 0

"""
这题 看这个文章
https://leetcode.cn/problems/lru-cache/solutions/12711/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/
原理解析的很详细

"""
# leetcode submit region begin(Prohibit modification and deletion)


class Node:

    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class NodeList:
    def __init__(self):
        self.size = 0
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.tail.prev = self.head

    def add(self,node:Node):
        tmp = self.tail.prev
        tmp.next = node
        node.next = self.tail
        node.prev = tmp
        self.tail.prev = node
        self.size += 1

    def removeFirst(self) -> Node:
        delNode = self.head.next
        if delNode:
            nextNode = delNode.next
            self.head.next = nextNode
            nextNode.prev = self.head
            self.size -= 1
        return delNode

    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1



class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.list = NodeList()
        self.cap = capacity

    def get(self, key: int) -> int:
        node = self.dict.get(key,None)
        if node is None:
            return -1
        else:
            self.list.remove(node)
            self.list.add(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key,None)
        if node is None:
            node = Node(key,value)

            self.dict[key] = node
            self.list.add(node)

            if self.list.size > self.cap:
                delNode = self.list.removeFirst()
                if delNode:
                    del self.dict[delNode.key]
        else:
            self.list.remove(node)
            self.list.add(node)
            node.value = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(2,1)
    obj.put(1,2)
    obj.put(2,3)
    print(obj.get(1))
    obj.put(3,3)
    print(obj.get(1))
    print(obj.get(2))
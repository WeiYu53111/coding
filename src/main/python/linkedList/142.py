# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/22/2022
# description :
"""
该题目最直观的做法是Hash表记录,但是空间复杂度为O(N).
双指针的空间复杂度为O(1),但是并不直观. 需要推理出对应的公式. 问题是在于如何说明相等的时候就是入口的地方

设 fast指针 走了 f步, slow指针走了 s步, 环形长度为b
相遇时 存在关系  f = 2s
同时 隐含关系是 快指针比慢指针多走了N圈. 因此f = s + nb
两式相减可得  2s- (s + nb) = 0 则 s = nb
假设 head到入口处长度为a , 入口到 相遇点为 c 则存在以下关系
s = a + c + xb  无论x是多少, 最终要  a+c+xb = nb。 因此 a+c必定是整数倍b.

因为 a + c = b , c点再走a步就能到达入口处了，a步刚好是从起点出发到入口处的距离。因此假设这时候有一个指针从head出发,慢指针从c点以相同的步数出发.
他们会在a点相遇.

所以相遇点 就是入口点 a

"""

from linkedList import ListNode
from linkedList import list_to_linkedList

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                tmp = head
                while tmp != slow:
                    tmp = tmp.next
                    slow = slow.next
                return tmp
        return None



if __name__ == '__main__':
    a = [1,8,3,4]
    head = list_to_linkedList(a)
    last = head.next.next.next
    last.next = head.next
    obj = Solution()
    node = obj.detectCycle(head)
    print(node.val)
# leetcode submit region end(Prohibit modification and deletion)


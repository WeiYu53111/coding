# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/19/2022
# description :  [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/submissions/)
from linkedList import ListNode
from linkedList import list_to_linkedList,print_linkedList


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev,prev.next = self,head
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            prev.next = b
            a.next = b.next
            b.next = a
            prev = a
        return self.next

if __name__ == '__main__':
    head = list_to_linkedList([1,2,3,4])
    obj = Solution()
    head = obj.swapPairs(head)
    print_linkedList(head)



# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/19/2022
# description :  [24. 两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/submissions/)


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


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
    a = [1,2,3,4]
    head = ListNode()
    cur = head
    for i in a:
        cur.next = ListNode(i)
        cur = cur.next
    obj = Solution()
    head = obj.swapPairs(head.next)
    while head:
        print(head.val)
        head = head.next



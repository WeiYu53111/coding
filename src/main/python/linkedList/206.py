# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/20/2022
# description :
# https://leetcode-cn.com/problems/reverse-linked-list/
# Definition for singly-linked list.


from linkedList import ListNode
from linkedList import list_to_linkedList, print_linkedList


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


if __name__ == '__main__':
    head = list_to_linkedList([1, 2, 3, 4, 5])
    obj = Solution()
    head = obj.reverseList(head)
    print_linkedList(head)

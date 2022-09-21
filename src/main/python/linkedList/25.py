# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/20/2022
# description :

from linkedList import ListNode
from linkedList import list_to_linkedList,print_linkedList

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if k == 1:
            return head

        prev,prev.next = self,head
        end = prev
        count = 0
        while end.next:
            end = end.next
            count += 1

            if count == 4:
                count = 0
                tmp = end.next
                end.next = None
                start = prev.next
                prev.next = self.reverse(start)
                start.next = tmp
                prev = start
                end = prev  ## 这步很关键,因为原来的end已经被修改了
        return self.next



    def reverse(self,head: ListNode) -> ListNode:
        prev,cur = None,head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9]
    head = list_to_linkedList(a)
    obj = Solution()
    head = obj.reverseKGroup(head,4)
    print_linkedList(head)
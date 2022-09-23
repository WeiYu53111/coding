# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/23/2022
# description :

from typing import Optional
from linkedList import ListNode,list_to_linkedList,print_linkedList

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1

        if list1.val >= list2.val:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2



# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':

    a = [1,4,5]
    b = [3,4,7]
    nodea = list_to_linkedList(a)
    nodeb = list_to_linkedList(b)
    obj = Solution()
    c = obj.mergeTwoLists(nodea,nodeb)
    print_linkedList(c)
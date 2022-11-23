# coding=utf-8
# ----------------
# author: weiyu
# create_time : 11/23/2022
# description :


# 给定一个单链表 L 的头节点 head ，单链表 L 表示为：
#
#
# L0 → L1 → … → Ln - 1 → Ln
#
#
#  请将其重新排列后变为：
#
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
#
#  不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
#  示例 1：
#
#
#
#
# 输入：head = [1,2,3,4]
# 输出：[1,4,2,3]
#
#  示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[1,5,2,4,3]
#
#
#
#  提示：
#
#
#  链表的长度范围为 [1, 5 * 10⁴]
#  1 <= node.val <= 1000
#
#
#  Related Topics 栈 递归 链表 双指针 👍 1085 👎 0

from typing import Optional
from linkedList import ListNode,list_to_linkedList,print_linkedList
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next
        size = len(nodes)
        left = 0
        right = size-1
        head = ListNode(-1)
        cur = head
        while left < right :
            a = nodes[left]
            b = nodes[right]
            cur.next = a
            a.next = b
            b.next = None
            cur = b
            left += 1
            right -= 1
        head = head.next
        if left == right:
            cur.next = nodes[left]
            nodes[left].next = None

if __name__ == '__main__':
    a = list_to_linkedList([1,2,3,4])
    obj = Solution()
    obj.reorderList(a)
    print_linkedList(a)



# leetcode submit region end(Prohibit modification and deletion)

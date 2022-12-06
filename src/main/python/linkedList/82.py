# coding=utf-8
# ----------------
# author: weiyu
# create_time : 12/5/2022
# description :


# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
#  示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
#  提示：
#
#
#  链表中节点数目在范围 [0, 300] 内
#  -100 <= Node.val <= 100
#  题目数据保证链表已经按升序 排列
#
#
#  Related Topics 链表 双指针 👍 1031 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from linkedList import ListNode
from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first = ListNode(-1)
        prev = first
        prev.next = head
        cur = head.next
        while cur:
            if cur.val == prev.val:
                a = cur.val
                while cur and cur == a:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return first.next


# leetcode submit region end(Prohibit modification and deletion)

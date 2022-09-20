# coding=utf-8
# ----------------
# author: weiyu
# create_time : 9/20/2022
# description :


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linkedList(a: list):
    """
    list 转换成 链表
    :param a:
    :return:
    """
    head = ListNode()
    cur = head
    for i in a:
        cur.next = ListNode(i)
        cur = cur.next
    return head.next


def print_linkedList(head : ListNode):
    while head:
        print(head.val)
        head = head.next
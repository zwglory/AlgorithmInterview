# -*- coding:utf-8 -*-
from __future__ import print_function
import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        pass

    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:   # 正常顺序
                cur = cur.next
                continue

            if p.next.val > val:  # 不需要每次都回到最开始
                p = dummy

            while p.next.val < val:
                p = p.next

            temp = cur.next
            cur.next = temp.next
            temp.next = p.next
            p.next = temp

        return dummy.next


def main():
    test_case = [2, 1]
    head = ListNode(test_case[0])
    p = head
    for t in test_case[1:]:
        p.next = ListNode(t)
        p = p.next

    solution = Solution()
    res = solution.insertionSortList(head)
    while res:
        print(res.val)
        res = res.next


if __name__ == '__main__':
    main()


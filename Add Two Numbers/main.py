from data_structure import ListNode
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        num1 = 0
        num2 = 0
        s = 0
        r = ListNode(None)
        cur = r
        while l1 or l2:
            if l1 and l2:
                s = l1.val + l2.val + res
            elif l1:
                s = l1.val + res
            else:
                s = l2.val + res

            res = s // 10
            remainder = s % 10
            cur.next = ListNode(remainder)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if res != 0:
            cur.next = ListNode(res)
        r = r.next
        return r
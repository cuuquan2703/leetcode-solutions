from data_structure import ListNode

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next  = head
        cur = head
        prevLeft = dummy
        for _ in range(left-1):
            prevLeft, cur = cur, cur.next

        prev = None
        for _ in range(right - left +1):
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp

        prevLeft.next.next = cur
        prevLeft.next = prev

        return dummy.next



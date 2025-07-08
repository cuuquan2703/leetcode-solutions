from data_structure import ListNode

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        
        if head == None:
            return head
        n = 1
        tail = head
        tmp = head
        while tmp.next != None:
            n += 1
            tmp = tmp.next
            tail = tail.next

        tail.next = head
        robin = n - (k % n)
        i = 0
        while i < robin:
            tail = tail.next
            head = head.next
            i+=1
            
        tail.next = None

        return head

        

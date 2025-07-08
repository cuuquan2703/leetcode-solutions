from data_structure import ListNode
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # Push all values from all linked lists into the heap
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        # If heap is empty, return None (no nodes)
        if not heap:
            return None
        
        # Create a dummy node to simplify result list construction
        dummy = ListNode()
        current = dummy
        
        # Pop values from heap and create linked list nodes
        while heap:
            val = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
        
        # Return the next node after dummy, which is the head of merged list
        return dummy.next
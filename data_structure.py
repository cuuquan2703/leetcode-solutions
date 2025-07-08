"""
Common data structures for LeetCode problems
"""

from typing import List, Union, Optional


class ListNode:
    """LeetCode ListNode class for linked list problems"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"
    
    @classmethod
    def from_list(cls, values: List[int]) -> Optional['ListNode']:
        """Create a linked list from a list of values"""
        if not values:
            return None
        
        head = cls(values[0])
        current = head
        for val in values[1:]:
            current.next = cls(val)
            current = current.next
        return head
    
    def to_list(self) -> List[int]:
        """Convert linked list to list of values"""
        result = []
        current = self
        while current:
            result.append(current.val)
            current = current.next
        return result


class TreeNode:
    """LeetCode TreeNode class for binary tree problems"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
    
    @classmethod
    def from_list(cls, values: List[Union[int, None]]) -> Optional['TreeNode']:
        """Create a binary tree from a list of values (level-order)"""
        if not values or values[0] is None:
            return None
        
        root = cls(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            # Left child
            if i < len(values) and values[i] is not None:
                node.left = cls(values[i])
                queue.append(node.left)
            i += 1
            
            # Right child
            if i < len(values) and values[i] is not None:
                node.right = cls(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def to_list(self) -> List[Union[int, None]]:
        """Convert binary tree to level-order list"""
        if not self:
            return []
        
        result = []
        queue = [self]
        
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        
        # Remove trailing None values
        while result and result[-1] is None:
            result.pop()
        
        return result

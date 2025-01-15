# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Start with no previous node
        current = head  # Start with the head node
        
        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the pointer
            prev = current  # Move prev one step forward
            current = next_node  # Move current one step forward
        
        return prev
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Step 1: Create a dummy node before head
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Use a pointer to traverse the list
        current = dummy

        # Step 3: Traverse and remove matching nodes
        while current.next:
            if current.next.val == val:
                # Skip the node if it matches 'val'
                current.next = current.next.next
            else:
                # Move to the next node if not matched
                current = current.next

        # Step 4: Return the new head (after dummy)
        return dummy.next

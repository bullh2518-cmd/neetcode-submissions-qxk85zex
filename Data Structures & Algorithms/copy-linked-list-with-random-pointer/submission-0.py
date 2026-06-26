"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
         # original node -> copied node
        old_to_copy = {}

        curr = head

        # First pass: create copied nodes
        while curr:
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Second pass: connect next and random pointers
        while curr:
            copy_node = old_to_copy[curr]

            if curr.next:
                copy_node.next = old_to_copy[curr.next]
            else:
                copy_node.next = None

            if curr.random:
                copy_node.random = old_to_copy[curr.random]
            else:
                copy_node.random = None

            curr = curr.next

        # Return copied head
        if head:
            return old_to_copy[head]
        else:
            return None
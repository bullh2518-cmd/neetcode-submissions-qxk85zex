# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        index = 0

        prev = dummy
        curr = head
        leng = 0
        first = head
        while first:
            leng += 1
            first = first.next
        target_index = leng - n
        while curr:
            if index == target_index:
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            index += 1

        return dummy.next
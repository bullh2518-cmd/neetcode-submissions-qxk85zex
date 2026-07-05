class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKth(curr, k):
            i = 0
            while curr and i < k:
                curr = curr.next
                i += 1
            return curr

        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = getKth(groupPrev, k)

            if not kth:
                break

            groupNext = kth.next

            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            tmp = groupPrev.next
            groupPrev.next = kth
            tmp.next = groupNext
            groupPrev = tmp

        return dummy.next
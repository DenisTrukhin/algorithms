```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s, f = head, head
        while f and f.next:
            s, f = s.next, f.next.next
        prev, curr = s, s.next
        prev.next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        while head.next:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True
```
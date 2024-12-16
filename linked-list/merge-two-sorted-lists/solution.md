```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 or list2:
            if list1 and not list2:
                next = list1
                list1 = list1.next
            elif list2 and not list1:
                next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                next = list1
                list1 = list1.next
            else:
                next = list2
                list2 = list2.next
            curr.next, curr = next, next
        return dummy.next
```
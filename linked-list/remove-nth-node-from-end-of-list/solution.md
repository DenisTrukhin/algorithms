```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        length, curr = 0, dummy
        while curr:
            length += 1
            curr = curr.next
        curr = dummy
        for _ in range(length - n - 1):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
```
Вариант 2 (Эталон)
```python
class Solution:
    # time:      O(n), где n - длина списка
    # mem(доп):  O(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(val=0, next=head)

        fast = dummyNode
        for i in range(n + 1):
            fast = fast.next

        slow = dummyNode
        while fast is not None:
            slow = slow.next
            fast = fast.next

        # удаляем вершину
        slow.next = slow.next.next

        return dummyNode.next
```
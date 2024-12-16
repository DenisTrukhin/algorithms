from heapq import heappush, heappop
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_list(arr: list[int]) -> ListNode:
    if not arr:
        return ListNode()
    last_node = ListNode(val=arr[-1])
    for val in arr[-2::-1]:
        last_node = ListNode(val=val, next=last_node)
    return last_node


def list_to_arr(node: ListNode) -> list[int]:
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda this, other: this.val < other.val
        h = []
        result = ListNode()
        curr = result

        for node in lists:
            if node:
                heappush(h, (node.val, node))

        while h:
            _, node = heappop(h)
            curr.next = node
            if node.next:
                heappush(h, (node.next.val, node.next))
            curr = curr.next

        return result.next


if __name__ == "__main__":
    s = Solution()
    actual = s.mergeKLists([array_to_list(arr) for arr in [[1,4,5],[1,3,4],[2,6]]])

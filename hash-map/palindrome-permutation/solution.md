```python
class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def can_permute_palindrome(self, s: str) -> bool:
        chars_count = {}
        for c in s:
            if c in chars_count:
                chars_count[c] += 1
            else:
                chars_count[c] = 1
        odd_count = sum(v & 1 for v in chars_count.values())
        return odd_count <= 1
```
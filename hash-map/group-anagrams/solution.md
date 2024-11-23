```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagram_list = "".join([f"{chr(c + ord('a'))}:{c};" for c in count])
            anagrams_map[anagram_list].append(s)
        return list(v for v in anagrams_map.values())
```
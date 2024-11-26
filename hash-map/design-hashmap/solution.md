```python
class MyHashMap:

    def __init__(self):
        self.size = 10_000
        self.map = [None] * self.size

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.map[index] is None:
            self.map[index] = [[key, value]]
        else:
            for pair in self.map[index]:
                if pair[0] == key:
                    pair[1] = value
                    return
            self.map[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.size
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.map[index] is not None:
            remove_index = None
            for i, pair in enumerate(self.map[index]):
                if pair[0] == key:
                    remove_index = i
                    break
            if remove_index is not None:
                self.map[index].pop(remove_index)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```
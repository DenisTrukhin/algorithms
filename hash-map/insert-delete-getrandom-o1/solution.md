```python
class RandomizedSet:

    def __init__(self):
        self.all_vals = []
        self.data_map = {}

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.all_vals)
        self.all_vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.data_map:
            remove_index = self.data_map[val]
            last_el = self.all_vals[-1]
            self.data_map[last_el] = remove_index
            self.all_vals[remove_index] = last_el
            self.all_vals.pop()
            self.data_map.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.all_vals)
```
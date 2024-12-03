```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        result = [0] * len(nums)
        idx = len(nums) - 1
        while l <= r:
            l_el = nums[l] if nums[l] >= 0 else -nums[l]
            r_el = nums[r] if nums[r] >= 0 else -nums[r]
            if l_el > r_el:
                result[idx] = l_el ** 2
                l += 1
            else:
                result[idx] = r_el ** 2
                r -= 1
            idx -= 1
        return result
```
*Эталон*
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # храним массив квадратов в убывающем порядке
        result = []
        p1 = 0 # указывает на начало массива
        p2 = len(nums) - 1 # указывает на конец массива
        while p1 <= p2:
            # больший элемент добавляем в конец ответа и двигаем указатель
            if abs(nums[p1]) > abs(nums[p2]):
                result.append(nums[p1] ** 2)
                p1 += 1
            else:
                result.append(nums[p2] ** 2)
                p2 -= 1
        # разворачиваем список, чтобы получить возрастающий порядок
        return reversed(result)
```
```golang
func sortedSquares(nums []int) []int {
	// храним массив квадратов в убывающем порядке
	result := make([]int, len(nums))
	p1 := 0 // указывает на начало массива
	p2 := len(nums) - 1 // указывает на конец массива
	i := len(nums) - 1
	for p1 <= p2 {
		// больший элемент добавляем в конец ответа и двигаем указатель
		if abs(nums[p1]) > abs(nums[p2]) {
			result[i] = nums[p1] * nums[p1]
			p1++
		} else {
			result[i] = nums[p2] * nums[p2]
			p2--
		}
		i--
	}
	return result
}
```
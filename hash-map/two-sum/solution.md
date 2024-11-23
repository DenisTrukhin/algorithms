```go
func twoSum(nums []int, target int) []int {
    mp := make(map[int]int)
    for i, n := range nums {
        add := target - n
        if ind, ok := mp[add]; ok {
            return []int{i, ind}
        }
        mp[n] = i
    }
    return []int{}
}
```
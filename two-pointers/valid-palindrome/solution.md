```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        is_palindrome = True
        while l < r:
            if not (s[l].isalnum() and s[r].isalnum()):
                if not s[l].isalnum():
                    l += 1
                if not s[r].isalnum():
                    r -= 1
            else:
                is_palindrome &= s[l].lower() == s[r].lower()
                l += 1
                r -= 1
        return is_palindrome
```
*Эталон*
```python
class Solution:
    # time:     O(n)
    # mem(доп): O(1)
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            # переходим к следующей букве пока l и r
            # не будут указывать на буквы или цифры
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            # оба символа - буквы или цифры
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
```
```golang
func isPalindrome(s string) bool {
    l, r := 0, len(s) - 1
    for l < r {
        // в условии сказано, что у нас ASCII символы, поэтому так делать можно
        leftRune, rightRune := rune(s[l]), rune(s[r])

        // переходим к следующей букве пока l и r
        // не будут указывать на буквы или цифры
        if !unicode.IsLetter(leftRune) && !unicode.IsDigit(leftRune) {
            l++
            continue
        }
        if !unicode.IsLetter(rightRune) && !unicode.IsNumber(rightRune) {
            r--
            continue
        }

        // оба символа - буквы или цифры
        if unicode.ToLower(leftRune) != unicode.ToLower(rightRune) {
            return false
        }
        l++
        r--
    }
    return true
}
```
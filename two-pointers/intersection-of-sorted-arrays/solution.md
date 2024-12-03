```python
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	def intersect(self, A, B):
	    p1 = p2 = 0
	    result = []
	    while p1 < len(A) and p2 < len(B):
	        if A[p1] == B[p2]:
	            result.append(A[p1])
	            p1, p2 = p1 + 1, p2 + 1
	        elif A[p1] < B[p2]:
	            p1 += 1
	        else:
	            p2 += 1
	    return result
```
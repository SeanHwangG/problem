# [LC_xor-queries-of-a-subarray](https://leetcode.com/problems/xor-queries-of-a-subarray)

```en
Given array arr of positive integers and array queries where queries[i] = [Li, Ri]
For each query i compute XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri])
```

```txt
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
```

## Solution

* py

  ```py
  def xorQueries(self, A, queries):
    for i in range(len(A) - 1):
      A[i + 1] ^= A[i]
    return [A[j] ^ A[i - 1] if i else A[j] for i, j in queries]
  ```

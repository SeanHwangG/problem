# [LC_orderly-queue](https://leetcode.com/problems/orderly-queue)

```en
Given string s and int k. Can choose one of first k letters of s and append it at end of string
Return lexicographically smallest string you could have after applying mentioned step any number of moves.
```

```txt
Input: s = "cba", k = 1
Output: "acb"

Input: s = "baaca", k = 3
Output: "aaabc"
```

## Solution

* Only swap operation is needed for Bubble sort, and when N > 1 you can swap two element

* py

  ```py
  def orderlyQueue(self, S, K):
    return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
  ```

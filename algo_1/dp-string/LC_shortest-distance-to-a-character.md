# [LC_shortest-distance-to-a-character](https://leetcode.com/problems/shortest-distance-to-a-character)

* en

  ```en
  Find closest occurrence of character c in s
  ```

* tc

  ```tc
  Input: s = "loveleetcode", c = "e"
  Output: [3,2,1,0,1,0,0,1,2,2,1,0]
  ```

## Solution

* py

  ```py
  def shortestToChar(self, S: str, C: str) -> List[int]:
    ret = [0 if s == C else len(S) for s in S]
    for i in range(1, len(S)):
      ret[i] = min(ret[i - 1] + 1, ret[i])
    for i in range(len(S) - 2, -1, -1):
      ret[i] = min(ret[i + 1] + 1, ret[i])
    return ret
  ```

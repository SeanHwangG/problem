# [LC_number-of-provinces](https://leetcode.com/problems/number-of-provinces)

* en

  ```en
  Given adjacency matrix, find total number of SCC
  ```

* tc

  ```tc
  Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
  Output: 2
  ```

## Solution

* Time: O(n**2)

* py

  ```py
  def findCircleNum(self, M: List[List[int]]):
    res, seen = 0, set()
    for i in range(len(M)):
      if i in seen: continue
      toSee = [i]
      while len(toSee):
        cur = toSee.pop()
        if cur not in seen:
          seen.add(cur)
          toSee += [j for j, v in enumerate(M[cur]) if v and j not in seen]
      res += 1
    return res
  ```

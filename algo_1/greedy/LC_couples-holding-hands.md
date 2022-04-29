# [LC_couples-holding-hands](https://leetcode.com/problems/couples-holding-hands)

Print minimum swaps to make partner sit next to each other (2 x N, 2 x N - 1)

```txt
Input: row = [0, 2, 1, 3]
Output: 1
```

## Solution

* py

```py
def minSwapsCouples(self, row: List[int]) -> int:
  n = len(row)
  pair = defaultdict(int)
  for i in range(0, len(row) - 1, 2):
    G[i] = i + 1
    G[i + 1] = i
  ans = 0
  for i in range(0, len(row) - 2, 2): #Traverse the array and swap if not with his/her pair
    if not pair[row[i]] == row[i+1]:
      ans += 1
      temp = row.index(pair[row[i]])
      row[i + 1], row[temp] = row[temp], row[i + 1]
  return ans
```

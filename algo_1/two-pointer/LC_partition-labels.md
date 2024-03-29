# [LC_partition-labels](https://leetcode.com/problems/partition-labels)

* en

  ```en
  String s of lowercase English letters is given
  Partition this string into as many parts as possible so that each letter appears in at most one part
  Return list of size of these parts
  ```

* tc

  ```tc
  Input: s = "ababcbacadefegdehijhklij"
  Output: [9,7,8]
  ```

## Solution

* py

  ```py
  def partitionLabels(self, s: str) -> List[int]:
    rightmost = {c : i for i, c in enumerate(s)}
    l, r = 0, 0
    result = []
    for i, letter in enumerate(s):
      r = max(r, rightmost[letter])
      if i == r:
        result += [r-l + 1]
        l = i + 1
    return result
  ```

# [LC_russian-doll-envelopes](https://leetcode.com/problems/russian-doll-envelopes)

* en

  ```en
  Given widths and heights find maximum number of envelopes you can Russian doll
  ```

* tc

  ```tc
  Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
  Output: 3   # [2,3] => [5,4] => [6,7]
  ```

## Solution

* py

  ```py
  def maxEnvelopes(self, en: List[List[int]]) -> int:
    en.sort(key = lambda x: (x[0], -x[1]))
    nums, lis = [j for _, j in en], []
    for current in nums:
      idx = bisect.bisect_left(lis, current)
      lis[idx:idx+1] = [current]
    return len(lis)
  ```

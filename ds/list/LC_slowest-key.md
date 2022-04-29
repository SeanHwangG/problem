# [LC_slowest-key](https://leetcode.com/problems/slowest-key)

Return the key of the keypress that had the longest duration
If there are multiple such keypresses, return the lexicographically largest key of the keypresses


```txt
Input: releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
Output: "a"  # Each letter took 12, 11, 13, 10, 16

Input: releaseTimes = [9,29,49,50], keysPressed = "cbcd"
Output: "c"  # c is larger than b
```

## Solution

* py

```py
def slowestKey(self, r, k):
  return max(zip(map(sub, r, [0, *r]), k))[1]
```

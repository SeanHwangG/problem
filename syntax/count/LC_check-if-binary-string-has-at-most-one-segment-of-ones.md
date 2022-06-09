# [LC_check-if-binary-string-has-at-most-one-segment-of-ones](https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones)

* en

  ```en
  Given a binary string s ​​​​​without leading zeros, return if s contains at most one contiguous segment of ones
  ```

* tc

  ```tc
  Input: "010"
  Output: False
  ```

## Solution

* go

  ```go
  func checkOnesSegment(s string) bool {
    return !strings.Contains(s, "01")
  }
  ```

* py

  ```py
  def checkOnesSegment(self, s: str) -> bool:
    return "01" not in s
  ```

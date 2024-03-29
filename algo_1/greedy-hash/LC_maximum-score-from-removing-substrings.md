# [LC_maximum-score-from-removing-substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings)

* en

  ```en
  Given a string s and two integers x and y. You can perform two types of operations any number of times
  Remove substring "ab" and gain x points
  For example, when removing "ab" from "cabxbae" it becomes "cxbae"
  Remove substring "ba" and gain y points
  For example, when removing "ba" from "cabxbae" it becomes "cabxe"
  Return the maximum points you can gain after applying the above operations on s
  ```

* tc

  ```tc
  Input: s = "aabbaaxybbaabb", x = 5, y = 4
  Output: 20
  ```

## Solution

* py

  ```py
  def maximumGain(self, s: str, x: int, y: int) -> int:
    if x < y:
      s = s.replace("a", "-").replace("b", "a").replace("-", "b")
      x, y = y, x
    seen = Counter()
    ans = 0
    for c in s + "x":
      if c in 'ab':
        if c == "b" and 0 < seen["a"]:
          ans += x
          seen["a"], seen["b"] = seen["a"] - 1, seen["b"] - 1
        seen[c] += 1
      else:
        ans += y * min(seen["a"], seen["b"])
        seen = Counter()

    return ans
  ```

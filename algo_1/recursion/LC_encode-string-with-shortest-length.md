# [LC_encode-string-with-shortest-length](https://leetcode.com/problems/encode-string-with-shortest-length)

* en

  ```en
  Given a string s, encode string such that its encoded length is the shortest.
  Encoding rule is: k[encoded_string], where encoded_string inside square brackets is being repeated k times
  ```

* tc

  ```tc
  Input: s = "aaaaa"
  Output: "5[a]"

  Input: s = "aabcaabcd"
  Output: "2[aabc]d"
  ```

## Solution

* py

  ```py
  @lru_cache(None)
  def encode(self, s: str) -> str:
    n = len(s)
    i = (s + s).find(s, 1)
    one = f'{n // i}[{self.encode(s[:i])}]' if i < n else s
    multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in range(1, n)]
    return min([s, one] + multi, key=len)
  ```

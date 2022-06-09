# [LC_group-shifted-strings](https://leetcode.com/problems/group-shifted-strings)

* en

  ```en
  Given array of strings strings, group all strings[i] that belong to the same shifting sequence
  ```

* tc

  ```tc
  Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
  Output:
  [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
  ```

## Solution

* py

  ```py
  def groupStrings(self, strings):
    key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
    return [list(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]
  ```

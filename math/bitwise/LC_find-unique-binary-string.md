# [LC_find-unique-binary-string](https://leetcode.com/problems/find-unique-binary-string)

Given array of strings nums containing n unique binary strings with length n
Return any binary string of length n that is not in nums

```txt
Input: nums = ["01","10"]
Output: "11"  # "00" also works

Input: nums = ["00","01"]
Output: "11"

Input: nums = ["111","011","001"]
Output: "101"
```

## Solution

* py

```py
def findDifferentBinaryString(self, nums: List[str]) -> str:
  return ''.join([str(1 ^ int(num[i])) for i, num in enumerate(nums)])
```

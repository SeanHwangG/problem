# [LC_counting-bits](https://leetcode.com/problems/counting-bits)

* en

  ```en
  Calculate number of 1's in their binary representation and return them as an array
  ```

* tc

  ```tc
  Input: n = 5
  Output: [0,1,1,2,1,2]
  ```

## Solution

* py

  ```py
  def countBits(self, num) -> List[int]:
    ret = [0] * (num + 1)
    for i in range(num + 1):
      ret[i] = ret[i // 2] + i % 2
    return ret
  ```

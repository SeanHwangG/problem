{% tabs %}{% tab title='LC_1643.md' %}

* Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down
* You are going to help Bob by providing instructions for him to reach destination
* The instructions are represented as a string, where each character is either:
  * 'H', meaning move horizontally (go right), or
  * 'V', meaning move vertically (go down).
* Multiple instructions will lead Bob to destination
  * For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.
* Bob has number k (1-indexed), and he want kth lexicographically smallest instructions that will lead him to destination
* Given array destination and k, return kth lexicographically smallest instructions that will take Bob to destination

```txt
Input: destination = [2,3], k = 1
Output: "HHHVV"

Input: destination = [2,3], k = 2
Output: "HHVHV"
```

{% endtab %}{% tab title='LC_1643.py' %}

```py
from math import comb
def kthSmallestPath(self, destination: List[int], k: int) -> str:
  r, c = destination
  ret, remDown = [], r
  for i in range(r + c):
    remSteps = r + c - (i + 1)
    com = comb(remSteps, remDown)
    if com >= k:
      ret.append("H")
    else:
      remDown -= 1
      k -= com
      ret.append("V")
  return ''.join(ret)
```

{% endtab %}{% endtabs %}

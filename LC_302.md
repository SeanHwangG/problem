{% tabs %}{% tab title='LC_302.md' %}

* Given an image that is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel
* Black pixels are connected (only one black region), Pixels are connected horizontally and vertically
* Given two integers x and y that represent location of one of black pixels
* Return area of smallest (axis-aligned) rectangle that encloses all black pixels

```txt
Input: image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
Output: 6

Input: image = [["1"]], x = 0, y = 0
Output: 1
```

{% endtab %}{% tab title='LC_302.py' %}

* Binary Search

```py
def minArea(self, image: List[List[str]], x: int, y: int) -> int:
  def first(lo, hi, check):
    class Checker:
      __getitem__ = staticmethod(check)
    return bisect.bisect(Checker(), False, lo, hi)
  top    = first(0, x,             lambda x: '1' in image[x])
  bottom = first(x, len(image),    lambda x: '1' not in image[x])
  left   = first(0, y,             lambda y: any(row[y] == '1' for row in image))
  right  = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))
  return (bottom - top) * (right - left)
```

{% endtab %}{% endtabs %}

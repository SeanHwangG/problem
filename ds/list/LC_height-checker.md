# [LC_height-checker](https://leetcode.com/problems/height-checker)

Return the number of indices where heights[i] != expected[i]

```txt
Input: heights = [1,1,4,2,1,3]
Output: 3  # 4, 1, 3

Input: heights = [5,1,2,3,4]
Output: 5

Input: heights = [1,2,3,4,5]
Output: 0
```

## Solution

* cpp

  ```cpp
  int heightChecker(vector<int>& h) {
    auto t = h;
    sort(t.begin(), t.end());
    return inner_product(h.begin(), h.end(), t.begin(), 0, plus<>(), not_equal_to<>());
  }
  ```

* py

  ```py
  def heightChecker(self, heights: List[int]) -> int:
      return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
  ```

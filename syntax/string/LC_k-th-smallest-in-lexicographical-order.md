# [LC_k-th-smallest-in-lexicographical-order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order)

Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n

```txt
Input: n = 13, k = 2
Output: 10 # lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Solution

* cpp

  ```cpp
  int findKthNumber(int n, int k) {
    int result = 1;
    for(--k; k > 0; ) {
      int count = 0;  // calculate #|{result, result*, result**, result***, ...}|
      for (long long first = static_cast<long long>(result), last = first + 1;
        first <= n; first *= 10, last *= 10) {           // while interval is not empty, increase a digit
        // valid interval = [first, last) union [first, n]
        count += static_cast<int>((min(n + 1LL, last) - first)); // add the length of interval
      }

      if (k >= count) { // skip {result, result*, result**, result***, ...} increase the current prefix
        ++result;
        k -= count;
      }
      else {      // not able to skip all of {result, result*, result**, result***, ...} search more detailedly
        result *= 10;
        --k;
      }
    }
    return result;
  };
  ```

* go

  ```go
  func min(a, b int) int {
    if a < b {
      return a
    }

    return b
  }
  func findGap(a, b, n int) int {
    gap := 0
    for (a <= n) {
      // n+1 => count node x0 too, which the gap includes it when n+1 is min
      // otherwise b is the min
      gap = gap + min(n+1, b) - a
      a = a * 10
      b = b * 10
    }

    return gap
  }
  func findKthNumber(n int, k int) int {
    current := 1
    k = k - 1 // target index is k-1

    for k > 0 { // break when reaching target index, where k == 0
      gap := findGap(current, current+1, n)

      // k completely cover the gap, move forward. if gap == k, loop will break next round since k == 0
      if gap <= k {
        k = k - gap
        current = current + 1
      } else {
        k-- // move one step down the tree
        current = current * 10
      }
    }

    return current
  }
  ```

* py

  ```py
  def findKthNumber(self, n, k):
    result = 1
    k -= 1
    while k > 0:
      count = 0
      lo, hi = result, result+1
      # prefix count
      # [result, result+1)
      # [result*10, (result+1)*10 )
      # [result*100, (result+1)*100 )
      while lo <= n:
        count += min(n+1, hi) - lo
        lo, hi = 10 * lo, 10 * hi
      if k >= count:
        result += 1
        k -= count
      else:
        result *= 10
        k -= 1
    return result
  ```

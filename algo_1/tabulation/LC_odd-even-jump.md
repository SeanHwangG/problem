# [LC_odd-even-jump](https://leetcode.com/problems/odd-even-jump)

* en

  ```en
  During odd-numbered jumps, jump to index j ST arr[i] <= arr[j] and arr[j] is smallest possible (value, index)
  During even-numbered jumps, jump to index j ST arr[i] >= arr[j] and arr[j] is largest possible (value, index)
  Return the number of indices where you can reach the end of the array
  ```

* tc

  ```tc
  Input: arr = [10,13,12,14,15]
  Output: 2
  ```

## Solution

* cpp
  * Time: O(NlogN)
  * Space: O(N)

  ```cpp
  int oddEvenJumps(vector<int>& A) {
    int n  = A.size(), res = 1;
    vector<int> higher(n), lower(n);
    higher[n - 1] = lower[n - 1] = 1;
    map<int, int> map {{A[n - 1], n - 1}};
    for (int i = n - 2; i >= 0; --i) {
      auto hi = map.lower_bound(A[i]), lo = map.upper_bound(A[i]);
      if (hi != map.end())   higher[i] = lower[hi->second];
      if (lo != map.begin()) lower[i] = higher[(--lo)->second];
      if (higher[i]) res++;
      map[A[i]] = i;
    }
    return res;
  }
  ```

* py

  ```py
  def oddEvenJumps(self, A):
    n = len(A)
    next_higher, next_lower = [0] * n, [0] * n

    stack = []
    for a, i in sorted([a, i] for i, a in enumerate(A)):
      while stack and stack[-1] < i:
        next_higher[stack.pop()] = i
      stack.append(i)

    stack = []
    for a, i in sorted([-a, i] for i, a in enumerate(A)):
      while stack and stack[-1] < i:
        next_lower[stack.pop()] = i
      stack.append(i)

    higher, lower = [0] * n, [0] * n
    higher[-1] = lower[-1] = 1
    for i in range(n - 1)[::-1]:
      higher[i] = lower[next_higher[i]]
      lower[i] = higher[next_lower[i]]
    return sum(higher)
  ```

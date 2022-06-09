# [LC_k-diff-pairs-in-an-array](https://leetcode.com/problems/k-diff-pairs-in-an-array)

* en

  ```en
  Given Array, find number of pairs with difference k
  ```

* tc

  ```tc
  Input: nums = [3,1,4,1,5], k = 2
  Output: 2
  ```

## Solution

* java

  ```java
  public int findPairs(int[] nums, int k) {
    Map<Integer, Integer> cnt = new HashMap<>();
    for (int x : nums)
      cnt.put(x, cnt.getOrDefault(x, 0) + 1);
    int res = 0;
    for (int x : cnt.keySet()) {
      if ((k > 0 && cnt.containsKey(x + k)) || (k == 0 && cnt.get(x) > 1))
        res++;
    }
    return res;
  }
  ```

* py

  ```py
  def findPairs(self, nums, k):
    c = collections.Counter(nums)
    return  sum(k > 0 and i + k in c or k == 0 and c[i] > 1 for i in c)
  ```

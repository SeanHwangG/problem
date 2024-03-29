# [LC_top-k-frequent-elements](https://leetcode.com/problems/top-k-frequent-elements)

* en

  ```en
  Return Top Kth frequent number
  ```

* tc

  ```tc
  Input: nums = [1,1,1,2,2,3], k = 2
  Output: [1,2]
  ```

## Solution

* cpp

  ```cpp
  int maxChunksToSorted(vector<int>& arr) {
    long int sum1 = 0, sum2 = 0, ans = 0;
    vector<int> t = arr;
    sort(t.begin(), t.end());
    for (int i = 0; i < arr.size(); i++) {
      sum1 += t[i];
      sum2 += arr[i];
      if (sum1 == sum2) ans++;
    }
    return int(ans);
  }
  ```

* py

  ```py
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    co = Counter(nums)
    return [a for a, b in co.most_common(k)]
  ```

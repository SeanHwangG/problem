* O(N); Worst case

```cpp
int findMin(vector<int> &num) {
  int lo = 0, hi = num.size() - 1, mid = 0;

  while (lo < hi) {
    if (num[mid] > num[hi])
      lo = mid + 1;
    else if (num[mid] < num[hi])
      hi = mid;
    else
      hi--;
  }

  return num[lo];
}
```

```py
def findMin(self, nums: List[int]) -> int:
  lo, hi = 0, len(nums)-1
  while hi > lo:
    mi = (lo + hi) // 2
    if nums[mi] < nums[hi]:
      hi = mi
    elif nums[mi] > nums[hi]:
      lo = mi + 1
    else:
      hi -= 1
  return nums[lo]
```

* Boyer-Moore Voting Algorithm
* Time; O(N)

```cpp
int majorityElement(vector<int>& nums) {
  int counter = 0, majority;
  for (int num : nums) {
    if (!counter)
      majority = num;
    counter += num == majority ? 1 : -1;
  }
  return majority;
}
```

```java
public int majorityElement(int[] nums) {
  int count = 0, candidate = 0;
  for (int num : nums) {
    if (count == 0)
      candidate = num;
    count += (num == candidate) ? 1 : -1;
  }
  return candidate;
}
```

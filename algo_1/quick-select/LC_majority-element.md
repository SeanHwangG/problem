# [LC_majority-element](https://leetcode.com/problems/majority-element)

Given an array nums of size n, return the majority element

```txt
Input: [3,2,3]
Output: 3
```

## Solution

* Boyer-Moore Voting Algorithm
* Time; O(N)

* cpp

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

* java

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

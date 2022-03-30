# [LC_sum-of-two-integers](https://leetcode.com/problems/sum-of-two-integers)

Given two integers a and b, return the sum of the two integers without using the operators + and -

```txt
Input: a = 1, b = 2
Output: 3
```

## Solution

```cpp
int getSum(int a, int b) {
  return b == 0? a: getSum(a ^ b, (a & b) << 1); // Be careful about the terminating condition;
}
```

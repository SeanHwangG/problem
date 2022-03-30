# [LC_maximum-population-year](https://leetcode.com/problems/maximum-population-year)

Given 2D int array logs where each logs[i] = [birthi, deathi] indicates birth and death years of ith person
Return earliest year with the maximum population

```txt
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
```

## Solution

```cpp
int maximumPopulation(vector<vector<int>>& logs) {
  int pop[2051] = {}, res = 0;
  for (auto &l : logs) {
    ++pop[l[0]];
    --pop[l[1]];
  }
  for (auto i = 1950; i < 2050; ++i) {
    pop[i] += pop[i - 1];
    res = pop[i] > pop[res] ? i : res;
  }
  return res;
}
```

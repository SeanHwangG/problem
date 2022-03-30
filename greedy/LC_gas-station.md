# [LC_gas-station](https://leetcode.com/problems/gas-station)

There are n gas stations along a circular route, where the amount of gas at ith station is gas[i]
Empty gas car starts from any of gas station, it costs cost[i] to travel from ith station to its next (i + 1)th station
Given two arrays gas and cost, return starting gas station's index that can travel around once in the clockwise direction
  Otherwise return -1. Solution is unique

```txt
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```

## Solution

```cpp
int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
  int total(0), subsum(INT_MAX), start(0);
  for (int i = 0; i < gas.size(); ++i) {
    total += gas[i] - cost[i];
    if(total < subsum) {
      subsum = total;
      start = i + 1;
    }
  }
  return (total < 0) ?  -1 : (start % gas.size());
}
```

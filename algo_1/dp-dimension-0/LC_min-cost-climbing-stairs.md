# [LC_min-cost-climbing-stairs](https://leetcode.com/problems/min-cost-climbing-stairs)

* en

  ```en
  Given an integer array cost where cost[i] is the cost of ith step on a staircase
  Once you pay the cost, you can either climb one or two steps
  Minimize the cost
  ```

* tc

  ```tc
  Input: cost = [10,15,20]
  Output: 15
  ```

## Solution

* cpp

  ```cpp
  int minCostClimbingStairs(vector<int>& cost) {
    int two_behind = cost[0], one_behind = cost[1];
    for (int i = 2; i < cost.size(); i++){
      int temp = one_behind;
      one_behind = min(two_behind, one_behind) + cost[i];
      two_behind = temp;
    }
    return min(one_behind, two_behind);
  }
  ```

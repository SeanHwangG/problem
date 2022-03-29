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

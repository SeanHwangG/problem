```cpp
int coinChange(vector<int>& coins, int amount) {
  sort(coins.begin(), coins.end());
  vector<int> dp(amount + 1, -1);
  dp[0] = 0;
  for (int i = 1; i <= amount; i++){
    int temp = INT_MAX;
    for (int coin: coins){
      if (coin > i) break;
      temp = min(temp, (dp[i - coin] == -1? temp: dp[i - coin] + 1));
    }
    dp[i] = (temp != INT_MAX? temp: -1);
  }
  return dp[amount];
}
```

```py
def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
  dp = [0] + [float('inf') for i in range(amount)]
  for i in range(1, amount+1):
    for coin in coins:
      if i - coin >= 0:
        dp[i] = min(dp[i], dp[i-coin] + 1)
  if dp[-1] == float('inf'):
    return -1
  return dp[-1]
```

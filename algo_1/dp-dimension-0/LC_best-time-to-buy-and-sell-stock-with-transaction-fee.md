# [LC_best-time-to-buy-and-sell-stock-with-transaction-fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee)

Array prices where prices[i] is price of given stock on ith day, and integer fee representing transaction fee
Find maximum profit you can achieve
You may complete as many transactions as you like, but you need to pay transaction fee for each transaction

```txt
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
```

## Solution

* py

  ```py
  def maxProfit(self, prices, fee):
    cash, hold = 0, -prices[0]
    for i in range(1, len(prices)):
      cash = max(cash, hold + prices[i] - fee)
      hold = max(hold, cash - prices[i])
    return cash
  ```

# [LC_best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown)

* en

  ```en
  Given an array prices where prices[i] is the price of a given stock on the ith day
  Find maximum profit can achieve
  You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times)
  After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day)
  ```

* tc

  ```tc
  Input: prices = [1,2,3,0,2]
  Output: 3
  ```

## Solution

* cpp

  ```cpp
  int maxProfit(vector<int>& prices) {
    if (prices.size() == 0) return 0;
    int cool = 0, nocool = 0, buy = -prices[0];
    for (int i = 1; i < prices.size(); i++){
      buy = max(nocool - prices[i], buy);
      nocool = max(nocool, cool);
      cool = buy + prices[i];
    }
    return max(cool, nocool);
  }
  ```

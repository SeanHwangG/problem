# [LC_best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

* en

  ```en
  You are given an array prices where prices[i] is the price of a given stock on ith day
  Maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stoc
  Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0

  ```

* tc

  ```tc
  Input: prices = [7,1,5,3,6,4]
  Output: 5  # Buy on day 2 (price = 1) and sell on day 5
  ```

## Solution

* java

  ```java
  public int maxProfit(int[] prices) {
    if (prices.length < 2)  return 0;
    int maxProfit = 0, min = prices[0];
    for (int i = 1; i < prices.length; i++){
      if (min > prices[i]) min = prices[i];
      else maxProfit = prices[i] - min > maxProfit? prices[i] - min: maxProfit;
    }
    return maxProfit;
  }
  ```

# [LC_richest-customer-wealth](https://leetcode.com/problems/richest-customer-wealth)

Given m x n int accounts where accounts[i][j] is amount of money i​​​​​​​​​​​th​​​​ customer has in j​​​​​​​​​​​th​​​​ bank
Return wealth that richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts


```txt
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
```

## Solution

* cpp

  ```cpp
  auto maximumWealth(auto const& accounts) -> int {
    return std::ranges::max(accounts | std::views::transform([](auto const& row) {
      return std::reduce(row.cbegin(), row.cend());
    }));
  }
  ```

* py

  ```py
  return max(map(sum, accounts))
  ```

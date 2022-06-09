# [LC_three-consecutive-odds](https://leetcode.com/problems/three-consecutive-odds)

* en

  ```en

  ```

* tc

  ```tc
  Input: arr = [2,6,4,1]
  Output: false

  Input: arr = [1,2,34,3,4,5,7,23,12]
  Output: true  # [5,7,23] are three consecutive odds.
  ```

## Solution

* cpp

  ```cpp
  auto three_consecutive_odds(auto const& arr) -> bool {
    auto const max_odds = arr
      | rv::group_by([](auto a, auto b) { return a % 2 == b % 2; })
      | rv::filter([](auto rng) { return rng[0] % 2 == 1; })
      | rv::transform(ranges::distance)
      | hs::maximum();
    return max_odds >= 3;
  }
  ```

* py

  ```py
  def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    return any(1 & a & b & c for a, b, c in zip(arr, arr[1:], arr[2:]))
  ```

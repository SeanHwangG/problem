# [LC_candy](https://leetcode.com/problems/candy)

* en

  ```en
  There are n children standing in a line. Each child is assigned a rating value given in int array ratings
  Giving candies to these children subjected to the following requirements:
    Each child must have at least one candy
    Children with a higher rating get more candies than their neighbors
  Return min number of candies you need to have to distribute the candies to the children
  ```

* tc

  ```tc
  Input: ratings = [1,0,2]
  Output: 5
  ```

## Solution

* Time, Space; O(N), O(N)

* py

  ```py
  def candy(self, ratings: List[int]) -> int:
    res = len(ratings) * [1]
    for i in range(1, len(ratings)):
      if ratings[i] > ratings[i-1]:
        res[i] = res[i - 1] + 1
    for i in range(len(ratings) - 1, 0, -1):
      if ratings[i - 1] > ratings[i]:
        res[i-1] = max(res[i - 1], res[i] + 1)
    return sum(res)
  ```

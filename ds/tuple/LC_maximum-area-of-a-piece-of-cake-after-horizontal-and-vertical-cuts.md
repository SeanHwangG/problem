# [LC_maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts)

* en

  ```en
  Given a rectangular cake of size h x w and two arrays of integers horizontals and verticals where:
  horizontals[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
  verticals[j] is the distance from the left of the rectangular cake to the jth vertical cut.
  Return max area of piece of cake after cut at each horizontal and vertical position, MOD 1e9+ 7
  ```

* tc

  ```tc
  Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
  Output: 4

  Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
  Output: 6
  ```

## Solution

* py

  ```py
  def maxArea(self, h: int, w: int, horizontals: List[int], verticals: List[int]) -> int:
    H = sorted([0] + horizontals + [h])
    V = sorted([0] + verticals + [w])
    return max(j - i for i, j in zip(H, H[1:])) * max(j - i for i,j in zip(V, V[1:])) % (10 ** 9 + 7)
  ```

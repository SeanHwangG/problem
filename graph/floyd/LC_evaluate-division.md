# [LC_evaluate-division](https://leetcode.com/problems/evaluate-division)

* en

  ```en
  Given an array of variable pairs equations and an array of real numbers values
    equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]
  Return answer to queries, where querie = [C, D] represents where you must find the answer for C / D = ?
  ```

* tc

  ```tc
  Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
  Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
  ```

## Solution

* Time; O(V^3)

* py

  ```py
  def calcEquation(self, equations : List[List[str]], values, queries) -> List[float]:
    quot = collections.defaultdict(dict)  # A/B=k is an edge A->B with weight k
    for (num, den), val in zip(equations, values):
      quot[num][num] = quot[den][den] = 1.0
      quot[num][den] = val
      quot[den][num] = 1 / val
    for k in quot:
      for i in quot[k]:
        for j in quot[k]:
          quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]
  ```

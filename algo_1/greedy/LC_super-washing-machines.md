# [LC_super-washing-machines](https://leetcode.com/problems/super-washing-machines)

* en

  ```en
  n super washing machines on a line. Initially, each washing machine has some dresses or is empty
  For each move, choose any m (1 <= m <= n) washing machines, and pass a dress of each washing machine to its adjacent
  Given an integer array machines representing # dresses in each washing machine from left to right on line
  Return minimum number of moves to make all washing machines have same number of dresses, -1 if impossible
  ```

* tc

  ```tc
  Input: machines = [1,0,5]
  Output: 3

  Input: machines = [0,3,0]
  Output: 2
  ```

## Solution

* py

  ```py
  def findMinMoves(self, machines):
    total, n = sum(machines), len(machines)
    if total % n: return -1
    target, res, toRight = total / n, 0, 0
    for m in machines:
      toRight = m + toRight - target
      res = max(res, abs(toRight), m - target)
    return res
  ```

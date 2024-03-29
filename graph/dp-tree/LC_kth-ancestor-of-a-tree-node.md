# [LC_kth-ancestor-of-a-tree-node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node)

* en

  ```en
  Given tree with n nodes from 0 (root) to n-1 in form of a parent array where parent[i] is parent of node i
  Implement getKthAncestor(int node, int k) to return k-th ancestor of given node (-1 if no such ancestor)
  ```

* tc

  ```tc
  Input:
  ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
  [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

  Output: [null,1,0,-1]
  ```

## Solution

* A is the parent in 1 step
* Based on this, we can find the parent in 2 steps, ... parent in 4 steps

* py

  ```py
  step = 15
  def __init__(self, n, A):
    A = dict(enumerate(A))
    jump = [A]
    for s in range(self.step):
      B = {}
      for i, a in A.items():
        if a in A:
          B[i] = A[a]
      jump.append(B)
      A = B
    self.jump = jump

  def getKthAncestor(self, x, k):
    step = self.step
    while k > 0 and x > -1:
      if k >= 1 << step:
        x = self.jump[step].get(x, -1)
        k -= 1 << step
      else:
        step -= 1
    return x
  ```

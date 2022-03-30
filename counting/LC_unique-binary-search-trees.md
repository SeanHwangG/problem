* Catalan numbers: $$ \frac{(2n)!}{(n + 1)!n!} $$
* Time, Space: O(N), O(1)

```py
def numTrees(self, n):
  # return factorial(2*n) // factorial(n) // factorial(n) // (n+1)
  res = [1]  + [0] * n
  for i in ange(1, n + 1):
    for j in range(i):
      # # unique BST with specified root F(i), is a product of number of BSTs for its left and right subtrees
      res[i] += res[j] * res[i - 1 - j]
  return res[n]
```
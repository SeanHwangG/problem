# [KT_symmetricorder](https://open.kattis.com/problems/symmetricorder)

Print name in symetric order respect to name length

```txt
Input: 7
Bo
Pat
Jean
Kevin
Claude
William
Marybeth
6
Jim
Ben
Zoe
Joey
Frederick
Annabelle
5
John
Bill
Fran
Stan
Cece
0
Output:
SET 1
Bo
Jean
Claude
Marybeth
William
Kevin
Pat
SET 2
Jim
Zoe
Frederick
Annabelle
Joey
Ben
SET 3
John
Fran
Cece
Stan
Bill
```

## Solution

* py

  ```py
  si = 0
  while n := int(input()) != 0:
    si += 1
    print(f"SET {si}")
    li = [input() for _ in range(n)]
    for i in range(0, n, 2):
      print(li[i])
    for i in range(1, n, 2):
      print(li[i])
  ```

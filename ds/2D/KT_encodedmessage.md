# [KT_encodedmessage](https://open.kattis.com/problems/encodedmessage)

```en
Encode string
```

```txt
Input: 3
RSTEEOTCP
eedARBtVrolsiesuAoReerles
EarSvyeqeBsuneMa

Output:
TOPSECRET
RosesAreRedVioletsAreBlue
SquaresMayBeEven

```

## Solution

* py

  ```py
  n = int(input())
  for _ in range(n):
    s = input()

    G = []
    m = int(len(s) ** 0.5)
    for i in range(m):
      G.append(s[i * m: (i + 1) * m])

    for j in reversed(range(m)):
      for i in range(m):
        print(G[i][j], end='')
    print()
  ```

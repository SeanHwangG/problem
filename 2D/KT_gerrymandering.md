# [KT_gerrymandering](https://open.kattis.com/problems/gerrymandering)

Given # precincts: party vote totals for each precinct, and how those precincts have been grouped into districts
For each district determine winner party and wasted votes for each party
determine efficiency gap between two parties over all districts
E(V, w_A, w_B)=\frac{|w_A-w_B|}{V}

```txt
Input: 5 3
1 100 200
2 100 99
3 100 50
3 100 50
2 100 98

Output: B 100 49
A 1 197
A 49 100
0.1965897693
```

## Solution

```py
n, m = map(int, input().split())
G = [[0, 0] for i in range(m)]
for i in range(n):
  a, b, c = map(int, input().split())
  G[a - 1][0] += b
  G[a - 1][1] += c

total_wa = 0
total_wb = 0
for a, b in G:
  if a < b:
    wa = a
    wb = b - (a + b) // 2 - 1
    print('B', wa, wb)
  else:
    wa = a - (a + b) // 2 - 1
    wb = b
    print('A', wa, wb)
  total_wa += wa
  total_wb += wb

print(abs(total_wa - total_wb) / sum(sum(l) for l in G))
```

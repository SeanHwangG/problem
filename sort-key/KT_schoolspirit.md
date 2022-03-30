# [KT_schoolspirit](https://open.kattis.com/problems/schoolspirit)

1/5 ∑_{i=0}^{n-1} s_i ⋅(4/5)^i

What is the average value of gi over all all n students?

```txt
Input:
3
500
120
75

Output:
128.8
89.06666666666666
```

## Solution

```py
n_team = int(input())
li = list(sorted([int(input()) for _ in range(n_team)], reverse=True))
score = 0
for i, n in enumerate(li):
  score += n * (0.8 ** i)
print(score / 5)
score = 0
for i, n in enumerate(li):
  up = i
  stay = (n_team - 1 - i)
  score += n * (up * (0.8 ** (i - 1)) + stay * (0.8 ** i))
print(score / 5 / n_team)
```

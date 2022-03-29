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

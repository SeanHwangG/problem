# [KT_dicecup](https://open.kattis.com/problems/dicecup)

Two dices with a, b sides
Print all numbers that appear with highest probability

```txt
Input: 12 20

Output:
13
14
15
16
17
18
19
20
21
```

## Solution

```py
a, b = map(int, input().split())
for i in range(min(a, b) + 1, max(a, b) + 2):
  print(i)
```

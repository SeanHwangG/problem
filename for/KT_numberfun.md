# [KT_numberfun](https://open.kattis.com/problems/numberfun)



```txt
Input: 6
1 2 3
2 24 12
5 3 1
9 16 7
7 2 14
12 4 2
Output: Possible
Possible
Impossible
Possible
Possible
Impossible
```

## Solution

```py
n_test = int(input())
for _ in range(n_test):
  a, b, c = map(int, input().split())
  if a + b == c or a - b == c or b - a == c or a * b == c or a / b == c or b / a == c:
    print("Possible")
  else:
    print("Impossible")
```

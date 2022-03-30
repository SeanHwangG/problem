# [KT_moscowdream](https://open.kattis.com/problems/moscowdream)



```txt
Input: 0 3 3 5
Output: NO
```

## Solution

```py
a, b, c, d = map(int, input().split())
print("NO" if a == 0 or b == 0 or c == 0 or a + b + c < d or d < 3 else "YES)
```

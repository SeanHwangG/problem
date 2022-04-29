# [KT_simonsays](https://open.kattis.com/problems/simonsays)



```txt
Input:
3
Simon says raise your right hand.
Lower your right hand.
Simon says raise your left hand.

Output:
 raise your right hand.
 raise your left hand.
```

## Solution

```py
N = int(input())
for _ in range(N):
  s = input()
  if s[:10] == "Simon says":
    print(s[10:])
```

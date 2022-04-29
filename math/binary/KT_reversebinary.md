# [KT_reversebinary](https://open.kattis.com/problems/reversebinary)

Print reversed binary

```txt
Input: 13
Output: 11
```

## Solution

* py

```py
a = bin(int(input()))[2:]
print(int(a[::-1],2))
```

# [KT_dicegame](https://open.kattis.com/problems/dicegame)



```txt
Input:
3
5 17
*****************
.............**$*
*B*A*P*C**X*Y*.X.
*y*x*a*p**$*$**$*
*****************
cz
5 11
*.*********
*...*...*x*
*X*.*.*.*.*
*$*...*...*
***********
0
7 7
*ABCDE*
X.....F
W.$$$.G
V.$$$.H
U.$$$.J
T.....K
*SQPML*
irony

Output:
3
1
0
```

## Solution

```py
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
if a < b:
  print('Emma')
elif b < a:
  print('Gunnar')
else:
  print('Tie')
```

# [KT_bela](https://open.kattis.com/problems/bela)



```txt
Input:
2 S
TH
9C
KS
QS
JS
TD
AD
JH

Output: 60
```

## Solution

* py

  ```py
  n_line, suit = input().split()
  n_line = int(n_line)
  dic = {'A': (11, 11), 'K': (4, 4), 'Q': (3, 3), 'J':(20, 2), 'T': (10, 10), '9': (14, 0), '8' : (0, 0), '7': (0, 0)}
  ret = 0
  for _ in range(n_line * 4):
    card = input()
    if card[1] == suit:
      ret += dic[card[0]][0]
    else:
      ret += dic[card[0]][1]
  print(ret)
  ```

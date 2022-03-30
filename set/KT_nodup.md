# [KT_nodup](https://open.kattis.com/problems/nodup)



```txt
Input: THE RAIN IN SPAIN
Output: yes
```

## Solution

```py
li = input().split()
print("yes" if len(set(li)) == len(li) else "no")
```
